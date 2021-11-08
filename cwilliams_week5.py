#!/usr/bin/env python3
#CIS254 Chris Williams Week 5 Assignment

#gather inputs: rate and initial investment
rate = input("Please enter an annualized interest rate without the % (e.g. \"2.95\" or \"26\"): ")
invest = input("Please enter an initial investment (e.g. \"199.95\" or \"2000\"): ")

#validate inputs are numeric and sane
try:
    ratef=float(rate)
    investf=float(invest)
    if ratef > 100:
        raise Exception("rate is insanely high")
    if ratef <= 0 or investf <= 0:
        raise Exception("values cannot be zero or negative")
except Exception as ex:
    print("Error: %s (while validating rate and investment)" % (ex))
    exit(1)
finally:
    pass

#set loop counter and accumulated value
years = 0
value = investf


#loop until investment doubles (or we get an error)
try:
    while value/investf < 2:
        years = years + 1
        #beauty of compounding interest!
        #also we remember to convert ratef from a percent to a decimal by dividing by 100 before we multiply accumulated value
        value = value + ((ratef/100) * value) 
    print("Investment of $%0.2f will double in %d years at the rate of %0.2f%%. Total value will be $%0.2f." % (investf, years, ratef, value))
except Exception as ex:
    print("Error: %s while annualizing interest." % (ex))
