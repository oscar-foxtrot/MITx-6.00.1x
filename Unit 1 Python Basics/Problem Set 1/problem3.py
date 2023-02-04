if len(s) >= 1:
    maxsub = s[0]
else:
    quit()

for i in range(len(s) - 1):
    j = i + 1
    while j <= len(s) - 1:
        if s[j-1] > s[j]:
            break
        j += 1
    if len(maxsub) < j - i:
        maxsub = s[i : j]
        
print('Longest substring in alphabetical order is: ' + maxsub)
