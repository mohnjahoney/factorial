from factorial import factorial

def test_factorial_1():
    """ some simple numbers"""    
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    
    
def test_factorial_2():
    """ some big numbers - test for overflow problems."""    
    assert factorial(10) == 3628800
    assert factorial(20) == 2432902008176640000
    
#    assert factorial(10**3) == 6
    

# def test_factorial_3():
#     """other cases that should be handled"""
#     
#     assert factorial(4.0) == 24
#     assert factorial(3.9999999999999999) = 24
#     assert factorial(4.0 + 0.0j) == 24
#     
# def test_factorial_4():
#     """cases that should throw exceptions"""
# 	
# 	assert factorial("this is a string") == SOMEKINDOFEXCEPTION
# 	assert factorial(-4) == SOMEKINDOFEXCEPTION
# 	assert factorial(-4.0) == SOMEKINDOFEXCEPTION
# 	assert factorial(-4.0 + 2.0j) == SOMEKINDOFEXCEPTION
# 	assert factorial([2,3,4,6]) == SOMEKINDOFEXCEPTION
# 	assert factorial(nan) == SOMEKINDOFEXCEPTION
# 	assert factorial(np.nan) == SOMEKINDOFEXCEPTION
# 	assert factorial(inf) == SOMEKINDOFEXCEPTION
# 	assert factorial(np.inf) == SOMEKINDOFEXCEPTION