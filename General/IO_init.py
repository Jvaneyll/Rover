#init libraries

import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

#init board
GPIO.setmode(GPIO.BOARD)
R_PWM_pin=int(12)
R_FW_pin=int(16)
R_RV_pin=int(18)

#init I/O
outpin = [R_PWM_pin,R_FW_pin,R_RV_pin]
GPIO.setup(outpin, GPIO.OUT)
