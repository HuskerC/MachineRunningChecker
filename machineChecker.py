#!/usr/bin/python

from pyEdimax.libedimax import EdimaxDevice
from mcutils.movingaverage import MovingAverage

import time

class MachineChecker:
	mPowerAverageThresholdOn = 0.0
	mPowerAverageThresholdOff = 0.0
	
	mMa = MovingAverage(8)
	mEdimaxDevice = None

	def __init__( self, thresholdOn, thresholdOff , machineHost ):
		self.mEdimaxDevice = EdimaxDevice(machineHost)
		self.mPowerAverageThresholdOn = thresholdOn
		self.mPowerAverageThresholdOff = thresholdOff
	
	def mainloop(self):
		while True:
			print "Average Value is %f" %  self.mMa.add(self.mEdimaxDevice.getCurrentPowerUsage()['watts'])
			if self.mMa.average() < self.mPowerAverageThresholdOff:
				print "Machine has finished"
				return
			time.sleep(2)		

def main():
	mc = MachineChecker(4,8,'192.168.176.34')
	mc.mainloop()

if __name__ == "__main__":
    main()

