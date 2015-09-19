import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# Set pin 4 to be an input pin
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

timer_counter = 0

while(True):
	if(GPIO.input(4) == 1):
		print "Bumper Left Hit"
	else:
		if (timer_counter % 10 == 0):
			print "Nothing Read"
			timer_counter = 0
	timer_counter = timer_counter + 1
	time.sleep(.1)	
