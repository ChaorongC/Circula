"""
Under development

This is a Python docstring, we can use reStructuredText syntax here!

.. code-block:: python

    # Import lumache
    import lumache

    # Call its only function
    get_random_ingredients(kind=["cheeses"])
"""

__version__ = "0.1.0"


class InvalidKindError(Exception):
    """Raised if the kind is invalid."""

    pass


def get_random_ingredients(kind=None):
    """
    Return a list of random ingredients as strings.

    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :raise lumache.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]
    """
    return ["shells", "gorgonzola", "parsley"]
    

def test_function(input='test', param2='test2'):
    """_summary_

    Parameters
    ----------
    input : str, optional
        _description_, by default 'test'
    param2 : str, optional
        _description_, by default 'test2'

    Returns
    -------
    _type_
        _description_
    """
    return 'testing %s %s ' % (input,param2)