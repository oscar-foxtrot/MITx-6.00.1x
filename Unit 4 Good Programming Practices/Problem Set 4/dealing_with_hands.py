def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    newhand = hand.copy()
    
    for c in word:
        newhand[c] -= 1
    
    keys_to_del = []
    for key in newhand:
        if newhand[key] == 0:
            keys_to_del.append(key)
            
    for elem in keys_to_del:
        del(newhand[elem])
        
    return newhand
