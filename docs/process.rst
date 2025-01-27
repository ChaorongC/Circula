Process
==========

.. _process:
Initial setup
-------------

To initialize a Circula program, use the ``circula init`` command. This command will create a new Circula project in the specified directory. The ``-r`` flag is required to specify the reference genome. The ``--ref-index`` and ``--ref-dict`` flags are optional and will create the reference genome index and dictionary files, respectively. ``--ref-index`` and ``--ref-dict`` flags are required for the alignment step and can be skipped if the reference genome index and dictionary files are already available at the directory enclosing the reference genome.

.. code-block:: bash

   reference = 'path/to/reference_genome.fa'
   project_dir = 'path/to/project_dir'

   circula init -r ${reference} --ref-index --ref-dict -o ${project_dir}

Single-step process
-------------------
If not assigned, the default output directory is the directory defined in the initialization step: *path/to/project_dir*. 

Each step can be run individually by specifying the step number with the ``-s`` flag an will output to its coreesponding directory, e.g. *trimming* will output to *path/to/project_dir/trimgalore_output*.


**1. Adapter trimmming (Trim Galore)**
   
   .. code-block:: bash

      input_r1='path/to/input_R1.fq.gz'
      input_r2='path/to/input_R2.fq.gz'

      circula process ${input_r1} ${input_r2} \
       -s 1 --prefix 'test_trimming' -@ 2 \
       --trimgalore-args '--clip_R1 10 --clip_R2 10 --three_prime_clip_R1 5 --three_prime_clip_R2 5'

**2. Genome alignment (bwa-meth)**
   
   .. code-block:: bash

      r1_trimmed='project_dir/trimgalore_outputtest_trimming_val_1.fq.gz'
      r2_trimmed='project_dir/trimgalore_outputtest_trimming_val_2.fq.gz'

      circula process ${r1_trimmed} ${r2_trimmed} -s 2 --prefix 'test_alignment' -@ 10

**3. Duplicate removal/marking (Picard)**
   
   .. code-block:: bash

      bam_input='project_dir/bwa_output/test_alignment.bam'

      circula process ${bam_input} -s 3 --prefix 'test_markdup' -@ 10

**4. Methyltion extraction (MethylDackel)**
   
   .. code-block:: bash

      bam_input='project_dir/picard_output/test_markdup.markdup.bam'

      circula process ${bam_input} -s 4 --prefix 'test_markdup' -@ 10


**5. Nucleosome occupancy calculation (DANPOS2)**
   
   By default, this process will calculate occupacny for all 1kb regions around transcription start sites (TSS) and polyadenylation sites (PAS). If ``-r`` is assigned, only regions in the bed file input will be calculated.

   .. code-block:: bash

      bam_input='project_dir/picard_output/test_markdup.markdup.bam'
      # default
      circula process ${bam_input} -s 5 --prefix 'test_occupancy' -@ 10
      # Calculate WPS for assigned regions
      circula process ${bam_input} -s 5 --prefix 'test_occupancy' -@ 10 -r 'path/to/regions.bed'


**6. Window protection score calculation**

   By default, this process will calculate WPS for all 1kb regions around transcription start sites (TSS) and polyadenylation sites (PAS). If ``-r`` is assigned, only regions in the bed file input will be calculated.

   .. code-block:: bash

      bam_input='project_dir/picard_output/test_markdup.markdup.bam'
      # default
      circula process ${bam_input} -s 6 --prefix 'test_wps' -@ 10
      # Calculate WPS for assigned regions
      circula process ${bam_input} -s 6 --prefix 'test_wps' -@ 10 -r 'path/to/regions.bed'



All-in-one process: from FASTQ file to epigenetic modalities calling
-------------------------------------------------------------------

Here is an example showing how to run the entire analysis pipeline with a single ``process`` command. The ``-s`` flag is required to specify the processing steps and is customizable based on the user's needs.
Addtional arguments can be passed to each step using the corresponding flags, e.g. ``--trimgalore-args`` for the trimming step. Output directories can be customized, e.g. ``--bwameth_output_dir`` for the alignment step.


   1. Adapter trimmming (Trim Galore)
   2. Genome alignment (bwa-meth)
   3. Duplicate removal/marking (Picard)
   4. Methylation extraction (MethylDackel)
   5. Nuclosome occupancy calculation (DANPOS2)
   6. Window protection score calculation

   .. code-block:: bash

      input_r1='path/to/input_R1.fq.gz'
      input_r2='path/to/input_R2.fq.gz'

      circula process ${input_r1} ${input_r2} \
       -s 1 2 3 4 5 6 --prefix 'test' -@ 20 \
       --trimgalore-args '--clip_R1 10 --clip_R2 10 --three_prime_clip_R1 5 --three_prime_clip_R2 5' \
       --bwameth_output_dir 'path/to/bwameth_output' \
       --methyldackel_output_dir 'path/to/methyldackel_output'
