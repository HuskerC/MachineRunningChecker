#!/usr/bin/python

import pyEdimax

class MachineChecker:
	mPowerAverageThresholdOn = 0.0
	mPowerAverageThresholdOff = 0.0
	
	edimaxDevice = None
	def __init__( self, thresholdOn, thresholdOff , machineHost ):
		edimaxDevice = pyEdimax.EdimaxDevice(machineHost)
		mPowerAverageThresholdOn = thresholdOn
		mPowerAverageThresholdOff = thresholdOff
	

def main():

if __name__ == "__main__":
    main()

