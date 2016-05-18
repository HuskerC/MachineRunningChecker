#!/usr/bin/python

from __future__ import division

class MovingAverage:

	mElements = []
	mWindowSize = 0
	
	def __init__(self, size = 5):
		self.mWindowSize = size

	def average( self ):
		sum = reduce(lambda x,y : x+y , self.mElements) #no magic, just apply the lamda function on every list element and the next element and so on.
		return sum/len(self.mElements)

	def add( self, number ):
		if len(self.mElements) == self.mWindowSize:
			self.mElements.pop(0)
		self.mElements.append(number)
		return self.average()
	

def test():
	ma = MovingAverage()
	ma.add( 2 )
	ma.add( 3 )
	ma.add( 3 )
	ma.add( 3 )
	ma.add( 3 ) 

	print ma.average()

if __name__ == '__main__':
	test()

