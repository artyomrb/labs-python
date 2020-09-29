def my_func(x):
    """
    >>> my_func(0)
    1.0
    >>> my_func(1)
    5.0
    """
    return float(((x**4)+(4**x)))
import doctest
doctest.testmod()
