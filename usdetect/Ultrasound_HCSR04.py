#init libraries

import RPi.GPIO as GPIO
import time
import statistics
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

#Initialize variables
n=int(input("How many distance measures do we take ? n= "))
raw=list()

#Create a function to run the cycle
def US_distance(n):
	i=1
	while i<=n:
		# Set trigger to False (Low)
		GPIO.output(22,0)
		
		# Allow module to settle
		time.sleep(0.5)

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
		raw.append(distance)
        
        #Increment i
        i=i+1
	print "Mean Distance : %.1f" % statistics.mean(raw)
	print "Median Distance : %.1f" % statistics.median_grouped(raw)
	print "Stddev Distance : %.1f" % statistics.pstdev(raw)
	print "Median Distance : %.1f" % statistics.median_grouped(raw)
	

# Reset GPIO settings
GPIO.cleanup()
