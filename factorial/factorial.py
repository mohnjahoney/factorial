# compute the factorial of a number

import numpy as np

def factorial(N):
    """
    Given an integer N, compute N factorial.
    N! = N * (N-1) * ... * 2 * 1.
    
    Parameters
    ----------
    N : integer
    
    Returns
    -------
    Nfact : integer
    
    Examples
    --------
    >>> a = 4
    >>> factorial_of_a_number(a)
    24
    
    TODO:
    - type check via assert
    - speedup
    - handle array input @vectorize
    - deal with overflow / set upperbound / handle nan nicely
    - use bigger int?
    - nosetest
    """
    
    return np.prod(range(1,N+1))
    
    
    
    