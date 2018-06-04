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

### Test consists of 10x10 measures at different distances and angles in front of a wall
## Angles to test
angles=[90,75,60,45,30,20,10]
## Distances to test
distances=[200,100,50,25,10,5]

for k in xrange(len(angles)):
	for l in xrange(len(distances)):
		raw_input(str(angles[k]) + " DEG - " + str(distances[l]) + " cm and press ENTER")
		
		#Initialize variables
		n=m=int(10)
		
		# Run the function in a cycle
		res=[]
		for i in xrange(n):
			raw=[]
			for j in xrange(m):
				a=US_distance()
				raw.append(a)
			res.append(raw)
			
		print(res)
		ang=np.tile(angles[k],n*m)
		print(ang)
		realdist=np.tile(distances[l],n*m)
		print(realdist)
		batch=np.repeat(range(1,m+1),n)
		print(batch)

# Reset GPIO settings
GPIO.cleanup()
