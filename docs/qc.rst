QC
==========

Methylation distribution
---------------------------

   .. code-block:: bash

      methylation_matrix='path/to/methylation_matrix.tsv'
      circula qc -s 1 ${methylation_matrix} -o ./methyaltion_dist.png


Fragment length distribution
----------------------------

   .. code-block:: bash

      bam_input='path/to/test_fragment_length.bam'
      circula qc -s 2 ${bam_input} -o ./fragment_len_dist.png


Dinucleotide frequency
----------------------

   .. code-block:: bash

      bam_input='path/to/test_fragment_length.bam'
      # check dinucleotide frequency for all 167bp fragments
      circula qc -s 3 ${bam_input} -f 167 -o ./fragment_len_dist.tsv

