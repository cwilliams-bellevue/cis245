#!/usr/bin/env python3
# initial script interpreter line missing, not required but usually used to allow script to run directly by name
# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: <unknown>, reviewer Christopher Williams chrwilliams2@my365.bellevue.edu
# Creation Date: <unknown>, Reviewed on 10/29/2021 CW
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	#these lines use improper indentation due to the litteral, the second-fourth lines and on are unusually indented
#	print('''You are in a land full of dragons. In front of you,
#	you see two caves. In one cave, the dragon is friendly
#	and will share his treasure with you. The other dragon
#	is greedy and hungry, and will eat you on sight.''')
	print('''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave():
# this line had incorrect indentation
#   cave = '' 
	cave = ''
	while cave != '1' and cave != '2':
		print('Which cave will you go into? (1 or 2)')
		cave = input()

	#the following line uses caves instead of cave, wrong variable name
	#return caves
	return cave

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	#this line sleeps for 3 seconds instead of 2
	#time.sleep(3)
	time.sleep(2)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		#the next line has a missing () requred in python3 but not in 2, 
		#other print statements use () so assuming we want to comply with version 3
		#print 'Gobbles you down in one bite!'
		print('Gobbles you down in one bite!')

playAgain = 'yes'
#this line has two a syntax errors, == operator is used to test equality
#while playAgain = 'yes' or playAgain = 'y':
while playAgain == 'yes' or playAgain == 'y':
	displayIntro()
	#the next line has an error calling the function without the proper case
	#caveNumber = choosecave()
	caveNumber = chooseCave()
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no, y/n)')
	playAgain = input()
	#inconsistent logic, we validate yes/y but not no/n
	#so we'll add a check here for valid input
	while playAgain not in {'yes', 'y', 'no', 'n'}:
		print('Invalid choice, try again.')
		print('Do you want to play again? (yes or no, y/n)')
		playAgain = input()
	# we make the next line consistent with the compound conditional testing for both no and n
	#if playAgain == "no":
	if playAgain == "no" or playAgain == 'n':
		#typo in the following line, planing vs playing
		#print("Thanks for planing")
		print("Thanks for playing")

