#init libraries

import RPi.GPIO as GPIO
import time
import numpy as np
GPIO.setwarnings(False)

#init board
GPIO.setmode(GPIO.BOARD)
US_trig=int(22)
US_echo=int(36)

#init I/O
##classical OUT pins
GPIO.setup(US_trig, GPIO.OUT)
##classical IN pins
inpin = US_echo
GPIO.setup(US_echo, GPIO.IN, GPIO.PUD_DOWN)
# Set trigger to False (Low)
GPIO.output(22,0)
# Allow module to settle
time.sleep(0.5)

#Initialize variables
n=int(input("How many distance measures do we take ? n= "))
raw=list()

#Create a function to measure distance and return value
def US_distance():
	# Send 10us pulse to trigger
	GPIO.output(US_trig, 1)
	time.sleep(0.00001)
	GPIO.output(US_trig, 0)
	start = time.time()
	while GPIO.input(US_echo)==0:
	    start = time.time()
	while GPIO.input(US_echo)==1:
	    stop = time.time()

	# Calculate pulse length
	elapsed = stop-start
	# Distance pulse travelled in that time is time
	# multiplied by the speed of sound (cm/s)
	distance = elapsed * 34000

	# That was the distance there and back so halve the value
	distance = distance / 2
	
	return(distance)

# Run the function in a cycle

for i in xrange(n):
	a=US_distance()
	raw.append(a)

# Calculate summary stats
npa=np.array(raw)
print "Mean Distance : %.1f" % np.nanmean(npa)
print "Stddev Distance : %.1f" % np.nanstd(raw)
print "Median Distance : %.1f" % np.nanmedian(raw)
print "Percentile 25th Distance : %.1f" % np.nanpercentile(raw,25)
print "Percentile 75th Distance : %.1f" % np.nanpercentile(raw,75)
print "Median Distance : %.1f" % np.nanmedian(raw)
print "Min Distance : %.1f" % np.nanmin(raw)
print "Max Distance : %.1f" % np.nanmax(raw)

# Reset GPIO settings
GPIO.cleanup()
