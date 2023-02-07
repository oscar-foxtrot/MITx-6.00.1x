lo = 0
hi = 100
print('Please think of a number between 0 and 100!')
# Proceed to div by 2 till the end
while (1):
    print('Is your secret number ' + str(int((hi + lo) / 2)) + '?')
    print(
        'Enter \'h\' to indicate the guess is too high. ' \
        'Enter \'l\' to indicate the guess is too low. ' \
        'Enter \'c\' to indicate I guessed correctly. ', end = '')
    c = input('')
    if c == 'l':
        lo = int((hi + lo) / 2)
    elif c == 'h':
        hi = int((hi + lo) / 2)
    elif c == 'c':
        print('Game over. Your secret number was: ' \
              + str(int((hi + lo) / 2)))
        break
    else:
        print('Sorry, I did not understand your input')
