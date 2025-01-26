Multimodal Epigenetic Sequence Analysis (MESA)
==========

.. _installation:

Installation
------------

To use Circula, first install it using pip or conda:

.. code-block:: console

   (.venv) $ pip install circula

# or

   (.venv) $ conda install -c conda-forge circula

Initial setup
-------------

To initialize a Circula program, use the ``circula init`` command. This command will create a new Circula project in the specified directory. The ``-r`` flag is required to specify the reference genome. The ``--ref-index`` and ``--ref-dict`` flags are optional and will create the reference genome index and dictionary files, respectively. ``--ref-index`` and ``--ref-dict`` flags are required for the alignment step and can be skipped if the reference genome index and dictionary files are already available at the directory enclosing the reference genome.

.. code-block:: bash

   $ circula init -r ${reference} --ref-index --ref-dict -o ./project_dir

All-in-one analysis example
---------------------------

After the initialization, you can run the entire analysis pipeline with a single ``process`` command. The ``-s`` flag is required to specify the processing steps and is customizable based on the user's needs.

1. Adapter trimmming (trim_galore)
2. Genome alignment (bwa-meth)
3. Duplicate removal/marking (picard)
4. Methylation extraction (methyldackel)
5. Nuclosome occupancy calculation (DANPOS2)
6. Window protection score calculation

.. code-block:: bash

   $ circula process ${input_r1} ${input_r2} -s 1 2 3 4 5 6 
    --prefix 'test_S2' -@ 10
    --trimgalore-args '--clip_R1 10 --clip_R2 10 --three_prime_clip_R1 5 --three_prime_clip_R2 5'

To retrieve a list of random ingredients,
you can use the ``circula.get_random_ingredients()`` function:

.. autofunction:: circula.get_random_ingredients

.. autofunction:: circula.test_function

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`circula.get_random_ingredients`
will raise an exception.

.. autoexception:: circula.InvalidKindError
