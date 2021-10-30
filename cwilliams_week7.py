#!/usr/bin/env python3
# Christopher Williams
# CIS245 Week 7 assignment

# findStockBySymbol
# takes a python dictionary and a symbol (string) as an argument 
# returns the stock price or None if not found
def findStockBySymbol(stocks,symbol):
	#make sure key is upper case
	symbol=symbol.upper()
	try:
		#return the value by key
		price = stocks[symbol]
		return(price)

	#if not found return None
	except KeyError:
		return(None)	

	#if some other error show warning and return None
	except Exception as ex:
		print("Some unhandled error ocurred: %s %s" % (ex, ex.type))
		return(None)

#define 10 stocks in a python dictionary
stockList = {
'AMD' : 103.88,
'FIS': 123.73,
'TTD': 72.58,
'AMAT': 140.8,
'BILL': 294.2,
'FTNT': 299.49,
'HUBS': 696.68,
'NET': 131.41,
'NVDA': 219,
'QCOM': 133.6
}

#start a loop until the user wishes to exit

while True:

	#prompt for a stock symbol or ? for a list or a blank to exit
	choice = input("Please enter a stock symbol to find the price.\nYou may also enter ? to see a list of stocks offered, or a blank (just hit enter) to quit. \nYour choice: ")

	#if blank we quit
	if choice == "":
		print("Quitting.")
		break

	#if ? we iterate through keys (symbols)
	if choice == "?":
		print("List of symbols available:")
		for smbl in stockList:
			print(smbl)
		continue

	val = findStockBySymbol(stockList,choice)
	if val == None:
		print("%s was not found.\n" % choice)
		continue
	else:
		print("The price for %s is %0.2f\n" % (choice.upper(), val))
		
		

