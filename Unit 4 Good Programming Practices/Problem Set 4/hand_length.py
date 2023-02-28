def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string -> int)
    returns: integer
    """
    # TO DO (in progress...)... <-- Remove this comment when you code this function
    res = 0
    for key0 in hand:
        res += hand[key0]
    return res
