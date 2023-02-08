def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    divis = min(a, b)
    while (divis > 1) and not(a % divis == 0 and b % divis == 0):
        divis -= 1
    return divis
