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


if __name__ == '__main__':
	main()