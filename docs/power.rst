Power analysis
==========

This power analysis tool is designed to estimate the sample size required to achieve a desired power level for a given effect size. The power analysis tool is based on the `Twist Human Methylome Panel <https://www.twistbioscience.com/products/ngs/fixed-panels/human-methylome-panel>`_ targets 3.98M CpG sites through 123 Mb of genomic content.

We obtained the p-value threshold, ``2.7e-08``, for differential analysis (pair-wise Wilcoxon rank-sum test for single CpGs) from 1,000 times of permutation test.

The follwing example shows how to estimate the power of biomarkers of 400 samples and a given effect size of 0.05. This command will output a power curve and a .tsv file containing the power analysis results.

.. code-block:: bash

   # Sample size=400, effect size=0.05, significance threshold= 2.7e-08
   circula power -o ./output -s 400 -e 0.05 --step-size 1000 -@ 10

.. image:: ../images/usage_power.png
   :alt: Power analysis example
   :width: 60%
   :align: center

.. figure:: ../images/usage_power.png
   :class: with-border
   :alt: Power analysis example
   :align: center
   :width: 60%
   
   power_analysis_ecdf_plot.png.

.. csv-table:: power_analysis_effect_size_cumulative_dist.tsv
   :file: ./power_analysis_effect_size_cumulative_dist.tsv
   :widths: 40, 60
   :header-rows: 1
   :align: center

Or use a customized p-value threshold:

.. code-block:: bash

   # Sample size=400, effect size=0.05, significance threshold= 1e-05
   circula power -o ./output -s 400 -e 0.05 --step-size 1000 -@ 10 --p-value-threshold 1e-05

