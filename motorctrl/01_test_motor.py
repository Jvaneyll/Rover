#Create a loop that runs n times to turn on and off the LED

#init libraries
print("initializing library and board")
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
import time
#init board
GPIO.setmode(GPIO.BOARD)
out1pin=int(16)
#init I/O
GPIO.setup(out1pin, GPIO.OUT)
print("init completed")

#Initialize variables
n=int(input("How many blink cycles do you want to run ? n= "))

#Create a function to run the cycle
def BlinkLED(n):
    i=1
    while i<=n:
        if i%2==0:
            GPIO.output(out1pin,True)
            time.sleep(0.5)
            GPIO.output(out1pin,False)
            time.sleep(0.5)
        else:
            GPIO.output(out1pin,True)
            time.sleep(0.2)
            GPIO.output(out1pin,False)
            time.sleep(0.8)
		    
        print(str(n-i) + " cycles left on " + str(n) + " requested")
        i=i+1
    print("blink cycles completed")

#Run the command
BlinkLED(n)
GPIO.cleanup()
	

