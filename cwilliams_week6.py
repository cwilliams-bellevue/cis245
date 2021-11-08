#!/usr/bin/env python3
#CIS254 Chris Williams Week 6 Assignment

import sys

#function miles2km: converts miles to kilometers
#arguments: miles is a float
#return value: kilometers is a float
#on error: returns none, prints error to stderr
def miles2km(miles):
	try:
		kms = miles / 0.62137
	except Exception as ex:
		sys.stderr.write("Error converting miles to kilometers: %s" % (ex))
		kms = None
	finally:
		return kms

#gather miles driven as input
driven = input("Please enter the number of miles driven as a whole number or a decimal: ")

#validate miles is numeric and positive
try:
    mi=float(driven)
    if mi <= 0:
        raise Exception("miles driven cannot be zero or negative")
except Exception as ex:
    print("Error: %s (while validating miles driven is a valid number)" % (ex))
    exit(1)
finally:
    pass

#attempt conversion
km = miles2km(mi)
#if it fails we exit
if km == None:
	print("Error encountered during conversion.")
	exit(2)


#show output including miles and km
print("Miles driven: %f Kilometers driven: %f" % (mi, km))
