def invest (amount, rate, years):
    """"Return the result of capitalize the amount of your money"""
    for n in range(1,years + 1):
        amount = amount + amount * rate
        print(f"Your amount of investment at the end of the year {n} is: {amount:,.2f}")
    return amount, rate, years
amount = float(input("Please enter the value for initial amount of investment: \n"))
rate = float(input("Please enter the value for rate in percentage: \n"))/100
years = int(input("Please enter the number of years for investment: \n"))
invest(amount, rate, years)
