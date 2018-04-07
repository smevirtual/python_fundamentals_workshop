"""
This module contains some common arithmetic operations.
"""

# Note that the "type hints" are optional. Type hints (the ": int" and the
# "-> int" portions of the function definition) are completely optional and they
# are a new feature of Python. However, going forward, if you design a function
# in Python that should only accept a certain data type (like "int" here), then
# you should consider using type hints.
#
# Check out https://www.python.org/dev/peps/pep-0484/ for more information.

def compute_sum(x: int, y: int) -> int:
    """
    Calculates the sum of two values.

    Parameters
    ----------
    x
        First value
    y
        Second value
    
    Returns
    -------
    Sum of the two provided values.
    """ 
    return x + y

def compute_difference(x: int, y: int) -> int:
    """
    Calculates the difference of two integers.

    Parameters
    ----------
    x
        First value
    y
        Second value
    
    Returns
    -------
    Difference of the two provided values.
    """
    return x - y