epsilon = 0.01

lo = balance / 12
hi = balance * ((1 +  annualInterestRate / 12) ** 12) / 12

while(True):
    curbalance = balance
    fmp = (hi + lo) / 2
    
    for i in range(1, 13):
        curbalance -= fmp
        curbalance *= (1 +  annualInterestRate / 12)
        
    if hi - lo <= epsilon:
        break
    else:
        if curbalance > 0:
            lo = fmp
        else:
            hi = fmp
        
print('Lowest Payment: ' + str(round(fmp, 2)) + '\n')
