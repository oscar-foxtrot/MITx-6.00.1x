for i in range(1, 13):
    # Minimum amount paid
    balance = balance * (1 - monthlyPaymentRate)
    # Then the interest is calculated
    balance = balance * (1 + annualInterestRate / 12)

print("Remaining balance: " + str(round(balance, 2)) + "\n")
