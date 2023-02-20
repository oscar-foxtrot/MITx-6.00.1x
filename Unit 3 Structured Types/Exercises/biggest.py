def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    maxkey = 'None'
    maxval = 0
    for i in aDict:
        tmp = len(aDict[i])
        if tmp >= maxval:
            maxval = tmp
            maxkey = i
    return maxkey
