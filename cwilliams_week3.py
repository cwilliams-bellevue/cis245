#!/usr/bin/env python3
#C Williams CIS245 Week 3 Assignment

print("Welcome to this week3 python script.")

while True:
    cname = input("Please enter the company name: ")
    try:
        if cname == None:
            raise Exception("blank value")
        if len(cname) < 2:
            raise Exception("too short")
    except Exception as ex:
        print("Error: %s for company name" % (ex))
    else:
        break


while True:
    cfeet = input("Please enter the number of feet of cable: ")
    try:
        if cfeet == None:
            raise Exception("blank value")
        feet = float(cfeet)
        if feet <= 0:
            raise Exception("not a positive value")
    except Exception as ex:
        print("Error: %s for feet of cable" % (ex))
    else:
        break

try:
    tcost = feet * .87
except Exception as ex:
    print("Error: %s calcuating total cost" % (ex))
else:
    print("The total cost for %s is $%0.2f" % (cname, tcost))


