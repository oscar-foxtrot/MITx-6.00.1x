def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.
    return value: doesn't return anything
    '''
    
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + \
          ' letters long.')
    delm = '------------'
    
    tries = 8  # Changable
    lettersGuessed = []
    mistakesMade = 0
    
    while(mistakesMade < tries and not isWordGuessed(secretWord, lettersGuessed)):
        print(delm)
        print('You have ' + str(tries - mistakesMade) + ' guesses left.')
        print('Available Letters: ' + getAvailableLetters(lettersGuessed))
        char = input('Please guess a letter: ')
        if char in secretWord:
            if char in lettersGuessed:
                print("Oops! You've already guessed that letter: " + \
                      getGuessedWord(secretWord, lettersGuessed))
            else:
                lettersGuessed.append(char)
                print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
        else:
            if char in lettersGuessed:
                print("Oops! You've already guessed that letter: " + \
                      getGuessedWord(secretWord, lettersGuessed))
            else:
                mistakesMade += 1
                lettersGuessed.append(char)
                print('Oops! That letter is not in my word: ' + \
                      getGuessedWord(secretWord, lettersGuessed))
        
    print(delm)
    if isWordGuessed(secretWord, lettersGuessed):
        print('Congratulations, you won!')
    else:
        print('Sorry, you ran out of guesses. The word was ' \
              + secretWord + '.')
    return
