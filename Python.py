#!/usr/bin/env python

import sys
import os
import commands

def main():
	print len(sys.argv)
	print 'Hello there', sys.argv[1]
	s = "search"
	print s.find('ea')
	print os.listdir('./')
	(status, output) = commands.getstatusoutput('ls -l') 
	print output

# Given two strings a, b, will return the list formed by all the possible concatenations.
def cross(a, b):
	return [s + t for s in a for t in b]

if __name__ == '__main__':
	main()
	# print cross('abc', '123')
	# print [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]
	# for i in range(len('123')):
	# 	print i
	# print sum([[1,2,3], [4, 5, 6]], [])

	a = [6, 9 ,2, 11]
	min = 100
	def find_min(a, b):
		if a < b:
			min = a
			return a
		else:
			min = b
			return b
	b = reduce(find_min, a)
	print(min)
	print(b)




'''

from utils import *



# Correct:

def only_choice(values):
    """Finalize all values that are the only choice for a unit.

    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
    """
    # TODO: Implement only choice strategy here
    #unSolved = [k for k in values.keys() if len(values[k]) != 1]
    
    digits = '123456789'
    for unit in unitlist:
        for digit in digits:
            digitAppearance = [box for box in unit if digit in values[box]]
            if len(digitAppearance) == 1:
                values[digitAppearance[0]] = digit
    
    return values

'''