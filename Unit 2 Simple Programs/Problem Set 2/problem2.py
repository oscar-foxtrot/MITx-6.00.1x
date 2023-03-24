fmp = 10
while(True):
    curbalance = balance
    for i in range(1, 13):
        curbalance -= fmp
        curbalance *= (1 +  annualInterestRate / 12)
    if curbalance < 0:
        break
    else:
        fmp += 10 
        
print(fmp)
