#!/usr/bin/python

from pyEdimax.libedimax import EdimaxDevice
from mcutils.movingaverage import MovingAverage

import argparse

import time

class MachineChecker:
	mPowerAverageThresholdOn = 0.0
	mPowerAverageThresholdOff = 0.0
	
	mMa = None
	mEdimaxDevice = None

	def __init__( self, thresholdOn, thresholdOff , numAvgValues ,machineHost ):
		self.mEdimaxDevice = EdimaxDevice(machineHost)
		self.mPowerAverageThresholdOn = thresholdOn
		self.mPowerAverageThresholdOff = thresholdOff
		self.mMa = MovingAverage(numAvgValues)
	
	def mainloop(self):
		while True:
			print "Average Value is %f" %  self.mMa.add(self.mEdimaxDevice.getCurrentPowerUsage()['watts'])
			if self.mMa.average() < self.mPowerAverageThresholdOff:
				print "Machine has finished"
				return
			time.sleep(2)		

def main():
	parser = argparse.ArgumentParser();
	parser.add_argument('--thresh-on',help='The switch on threshold',required=True)
	parser.add_argument('--thresh-off',help='The switch off threshold',required=True)
	parser.add_argument('--average-numbers',help='The number of values to calculate the average on. Default is 8.',default='8')
	parser.add_argument('host',help='hostname')
	args= parser.parse_args()
	#print args.thresh_on
	mc = MachineChecker(float(args.thresh_on),float(args.thresh_off),int(args.average_numbers),args.host)
	mc.mainloop()

if __name__ == "__main__":
    main()

