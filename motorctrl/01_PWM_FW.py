#init libraries

import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

#init board
GPIO.setmode(GPIO.BOARD)
L_PWM_pin=int(12)
L_FW_pin=int(16)
L_RV_pin=int(18)
R_PWM_pin=int(33)
R_FW_pin=int(37)
R_RV_pin=int(15)

#init I/O

##classical OUT pins
outpin = [R_PWM_pin,R_FW_pin,R_RV_pin,L_PWM_pin,L_FW_pin,L_RV_pin]
GPIO.setup(outpin, GPIO.OUT)

##classical IN pins

#PWM pins
##Initialize PWM frequency variable
PWM_freq=int(5000)
launch_time=0.1

##Set PWM pins
r = GPIO.PWM(R_PWM_pin, PWM_freq)
l = GPIO.PWM(L_PWM_pin, PWM_freq)

# Safety checks
## Motors in stopped mode
GPIO.output(outpin, GPIO.LOW)
r.stop()
l.stop()

#Create motor control function through H bridge
## Sens de rotation du moteur
STOP = 1
FWD = 2
REV = 3

def Inactive():
	""" Deactivate H bridge """
	GPIO.output(R_PWM_pin, GPIO.LOW)
	if(L_PWM_pin != R_PWM_pin):
		GPIO.output(L_PWM_pin, GPIO.LOW)
		
def RMotDir(rot):
	""" Define rotation direction for right motor """
	if(rot == FWD):
		GPIO.output(R_FW_pin, GPIO.HIGH)
		GPIO.output(R_RV_pin, GPIO.LOW)
	elif(rot == REV):
		GPIO.output(R_FW_pin, GPIO.LOW)
		GPIO.output(R_RV_pin, GPIO.HIGH)
	elif(rot == STOP):
		GPIO.output(R_FW_pin, GPIO.LOW)
		GPIO.output(R_RV_pin, GPIO.LOW)	

def LMotDir(rot):
	""" Define rotation direction for left motor """
	if(rot == FWD):
		GPIO.output(L_FW_pin, GPIO.HIGH)
		GPIO.output(L_RV_pin, GPIO.LOW)
	elif(rot == REV):
		GPIO.output(L_FW_pin, GPIO.LOW)
		GPIO.output(L_RV_pin, GPIO.HIGH)
	elif(rot == STOP):
		GPIO.output(L_FW_pin, GPIO.LOW)
		GPIO.output(L_RV_pin, GPIO.LOW)

def RActive(Rdc):
	""" Activate H bridge """
	r = GPIO.PWM(R_PWM_pin, PWM_freq)
	#Launch motor
	sdc=100
	r.start(sdc)
	time.sleep(launch_time)
	#change the duty cycle to desired one
	#Rdc=50
	r.ChangeDutyCycle(Rdc)  # where 0.0 <= Rdc <= 100.0
	
def LActive(Ldc):
	l = GPIO.PWM(L_PWM_pin, PWM_freq)
	#Launch motor
	sdc=100
	l.start(sdc)
	time.sleep(launch_time)
	#change the duty cycle to desired one
	#Ldc=50
	l.ChangeDutyCycle(Ldc)
	
def Active(dc):
	""" Activation des pont-H """
	r = GPIO.PWM(R_PWM_pin, PWM_freq)
	l = GPIO.PWM(L_PWM_pin, PWM_freq)
	#Launch motor
	sdc=100
	r.start(sdc)
	l.start(sdc)
	time.sleep(launch_time)
	#change the duty cycle to desired one
	r.ChangeDutyCycle(dc)
	l.ChangeDutyCycle(dc)  # where 0.0 <= dc <= 100.0
	time.sleep(5)

def Forward(dc):
	RMotDir(FWD)
	LMotDir(FWD)
	Active(dc)
	
def Reverse(dc):
	RMotDir(REV)
	LMotDir(REV)
	Active(dc)
	
def Left(dc):
	RMotDir(FWD)
	LMotDir(REV)
	Active(dc)

def Right(dc):
	RMotDir(REV)
	LMotDir(FWD)
	Active(dc)
		
if __name__ == '__main__':
	Inactive()
	Forward(30)
	Reverse(30)
	Left(30)
	Right(30)
	Inactive()
	GPIO.cleanup()
