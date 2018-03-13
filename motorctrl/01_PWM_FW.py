#Test basic PWM function with LED

#init libraries
print("initializing library and board")
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
import time
#init board
GPIO.setmode(GPIO.BOARD)
out1pin=int(12)
#init I/O
GPIO.setup(out1pin, GPIO.OUT)
print("init completed")

#Initialize variables
freq=float(input("What PWM frequency to use (Hz) ?"))

#Create a function to run the cycle
def PWMLED(freq):
	#create a PWM instance:
	p = GPIO.PWM(out1pin, freq)
	dc=0
	#start PWM:
	p.start(dc)
	#change the duty cycle every 0.5sec to make the whole cycle
	while dc<100:
		dc=dc+10
		p.ChangeDutyCycle(dc)  # where 0.0 <= dc <= 100.0
		time.sleep(1)
	#stop PWM:
	p.stop()

#Run the command
PWMLED(freq)
GPIO.cleanup()
	

