import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
# GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# A-B
GPIO.setup(6, GPIO.OUT)

# A-A
GPIO.setup(13, GPIO.OUT)


GPIO.output(6, True)
GPIO.output(13, False)

#while(True):
#	print GPIO.input(16)
#	time.sleep(1)



