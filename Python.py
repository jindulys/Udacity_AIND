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
	print cross('abc', '123')
	print [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]
	for i in range(len('123')):
		print i
	print sum([[1,2,3], [4, 5, 6]])