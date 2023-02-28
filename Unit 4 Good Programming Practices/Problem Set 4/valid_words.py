def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    if word.lower() not in wordList:
        return False
    newhand = hand.copy()
    try:
        for c in word:
            newhand[c] -= 1
    except KeyError:
        return False
    
    for key in newhand:
        if newhand[key] < 0:
            return False
    
    return True
