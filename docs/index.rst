Circula: an all-in-one command-line toolkit for cell-free DNA analysis
======================================================================

Circula is a command-line toolkit for cell-free DNA analysis. It is designed to be a one-stop solution for processing cell-free DNA data from raw FASTQ files to machine learning model for disease detection/prediction. Circula is built on top of popular or customized bioinformatics tools such as BWA, trim_galore, and MESA. It is designed to be easy to use, with a simple command-line interface that allows users to run the entire analysis pipeline with a single command, or run customized analysis with ease.

.. image:: https://readthedocs.org/projects/example-sphinx-basic/badge/?version=latest
    :target: https://example-sphinx-basic.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: ../images/intro_workflow.png
    :alt: Circula workflow
    :align: center

Installation
------------

To use Circula, first install it using pip or conda:

.. code-block:: console

    $ pip install circula

OR

.. code-block:: console

    $ conda install -c conda-forge circula
Check out the :doc:`usage` section for further information, including
how to :ref:`installation` the project.

.. note::

   This project is under active development.

Contents
--------

.. toctree::

   About Circula <self>
   usage
   process
   qc
   power
   mesa
   analysis
   api
