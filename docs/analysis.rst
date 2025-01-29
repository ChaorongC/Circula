Basic analysis
==========

   .. image:: ../images/analysis_tba.png
      :alt: Basic analysis TBA
      :width: 90%
      :align: center

Principal component analysis (PCA)
------------

To use Circula, first install it using pip or conda:

.. code-block:: console

   $ pip install circula

OR

.. code-block:: console

   $ conda install -c conda-forge circula

Differential analysis
-------------

To initialize a Circula program, use the ``circula init`` command. This command will create a new Circula project in the specified directory. The ``-r`` flag is required to specify the reference genome. The ``--ref-index`` and ``--ref-dict`` flags are optional and will create the reference genome index and dictionary files, respectively. ``--ref-index`` and ``--ref-dict`` flags are required for the alignment step and can be skipped if the reference genome index and dictionary files are already available at the directory enclosing the reference genome.

.. code-block:: bash

   circula init -r ${reference} --ref-index --ref-dict -o ./project_dir

Clustered heatmap
---------------------------

