def invest(amount, rate, years):
    amount = int(input("$: "))
    rate = float(input("%: "))
    years = int(input("Years: "))
    dolya = rate/100

    i = 0
    while i < years:
        i+=1
        amount_per = amount*dolya
        amount = amount+amount_per
        
        print("year ", i, ": $", round(amount, 2))

amount =0
rate = 0
years = 0


invest(amount, rate, years)

