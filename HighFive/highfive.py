import RPi.GPIO as GPIO
import time
import signal
import sys


# All IO specified in BCM pinout
INPUT_MOTION = 20
OUTPUT_LED = 21
OUTPUT_SERVO = 12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(INPUT_MOTION, GPIO.IN)                     #Read signal from PIR motion sensor
GPIO.setup(OUTPUT_LED, GPIO.OUT, initial=0)         #LED output pin
GPIO.setup(OUTPUT_SERVO, GPIO.OUT)						#Servo output pin

def signal_handler(signal, frame):
        print('EXIT: Cleaning Up')
        GPIO.cleanup()
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)


pwm=GPIO.PWM(OUTPUT_SERVO,50)
pwm.start(5)
pwm.ChangeDutyCycle(7.5)

while True:
	
	GPIO.wait_for_edge(INPUT_MOTION, GPIO.RISING)
	print "High Five!"
	GPIO.output(OUTPUT_LED, 1) #Turn on LED

	GPIO.wait_for_edge(INPUT_MOTION, GPIO.FALLING)
	print "Recoil"
	GPIO.output(OUTPUT_LED, 0) #Turn off LED


