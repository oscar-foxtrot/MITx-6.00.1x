def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    res = 1
    while exp > 0:
        res *= base
        exp -= 1
    return res
