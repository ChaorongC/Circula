QuickStart
=====

.. _installation:

Installation
------------

To use Circula, first install it using pip or conda:

.. code-block:: console

   (.venv) $ pip install circula
   # or
   (.venv) $ conda install -c conda-forge circula

All-in-one analysis example
------------

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

.. autofunction:: lumache.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError

For example:

>>> import lumache
>>> lumache.get_random_ingredients()
>>> ['shells', 'gorgonzola', 'parsley']
>>>
>>
