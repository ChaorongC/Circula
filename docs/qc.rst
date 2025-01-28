QC
==========

Methylation distribution
---------------------------

   .. code-block:: bash

      methylation_matrix='path/to/methylation_matrix.tsv'
      circula qc -s 1 ${methylation_matrix} -o ./methyaltion_dist.png

   .. image:: ../images/qc_methylation_dist.png
      :alt: Methyaltion distribution plot
      :width: 60%

Fragment length distribution
----------------------------

   .. code-block:: bash

      bam_input1='path/to/test_fragment_length1.bam'
      bam_input2='path/to/test_fragment_length2.bam'
      # Plot fragment length distribution for single bam file
      circula qc -s 2 -o ./output/frag_dist.png -@ 5 --title 'test_fragment_dist' ${bam_input1} 
      # Plot average fragment length distribution for multiple bam files
      circula qc -s 2 -o ./output/frag_dist.png -@ 5 --title 'test_fragment_dist' ${bam_input1} ${bam_input2}


   .. image:: ../images/qc_fragment_dist.png
      :alt: fragment length distribution plot
      :width: 60%

Dinucleotide frequency
----------------------

   .. code-block:: bash
      
      ref = 'path/to/reference_genome.fa'
      bam_input1='path/to/test_dinucleotide_frequqncy1.bam'
      bam_input2='path/to/test_dinucleotide_frequqncy2.bam'
      # check dinucleotide frequency for all 167bp fragments
      circula qc -s 3 -f 166 -o ./output/dinucleotide_frequency_dist.png -@ 8 -r ${ref} ${bam_input1} ${bam_input2}

   .. image:: ../images/qc_dinucleotide_dist.png
      :alt: dinucleotide frequency distribution plot
      :width: 60%
