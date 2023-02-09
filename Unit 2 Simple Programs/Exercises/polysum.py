import math
def polysum(n, s):
    '''
    This function calculates the sum of the square of teh perimeter and the area
    of the polygon specified by the parameters n, s. 
    
    parameters:
    int n: number of sides
    float s: length of a side
    
    returns: int: square of the polygon + (perimeter of the polygon)**2
    '''
    sum = 0.25 * n * s**2 / math.tan(math.pi / n) + (n * s)**2
    return round(sum, 4)
