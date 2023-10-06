homePrice = 1200000
downPayment = 240000
Principle = homePrice - downPayment
rate = 0.06  #6%
numMonths = 12
totalYears = 30
mortgage = (Principle * rate /
            numMonths) / (1 -
                          (1 + rate / numMonths)**(-numMonths * totalYears))

print(mortgage)