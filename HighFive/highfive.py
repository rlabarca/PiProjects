import RPi.GPIO as GPIO
import time
import signal
import sys


# All IO specified in BCM pinout
INPUT_MOTION = 20
OUTPUT_LED = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN)                     #Read signal from PIR motion sensor
GPIO.setup(21, GPIO.OUT, initial=0)         #LED output pin

def signal_handler(signal, frame):
        print('EXIT: Cleaning Up')
        GPIO.cleanup()
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

while True:
	
	GPIO.wait_for_edge(INPUT_MOTION, GPIO.RISING)
	print "High Five!"
	GPIO.output(OUTPUT_LED, 1) #Turn on LED

	GPIO.wait_for_edge(INPUT_MOTION, GPIO.FALLING)
	print "Recoil"
	GPIO.output(OUTPUT_LED, 0) #Turn off LED


