def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    res = 0
    for i in aDict:
        res += len(aDict[i])
    return res
