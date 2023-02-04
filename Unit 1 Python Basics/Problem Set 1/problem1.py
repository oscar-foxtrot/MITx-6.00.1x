counter = 0
for char in s:
    if char == 'o' or char == 'u' or char == 'a' \
        or char == 'e' or char == 'i':
        counter += 1
print('Number of vowels: ' + str(counter))
