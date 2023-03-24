def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    res = ''
    for c in 'abcdefghijklmnopqrstuvwxyz':
        if c not in lettersGuessed:
            res += c 
    return res
