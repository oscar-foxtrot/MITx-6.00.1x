def genPrimes():
    found_primes = []
    curnum = 2
    while True:
        found = False
        for i in found_primes:
            if curnum % i == 0:
                found = True
                break
        if not found:
            found_primes.append(curnum)
            yield curnum
        curnum += 1
