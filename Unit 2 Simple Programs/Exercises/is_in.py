def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) == 0:
        return False
    elif aStr[len(aStr) // 2] == char:
        return True
    else:
        if char > aStr[len(aStr) // 2]:
            return isIn(char, aStr[(len(aStr) // 2 + 1) :])
        else:
            return isIn(char, aStr[: (len(aStr) // 2)])
