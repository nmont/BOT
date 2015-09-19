import nxppy
import time 

mifare = nxppy.Mifare()
timer_counter = 0

# Print the card UIDs as the are detected
while True:
	try:
		uid = mifare.select()
		print(uid)
	except nxppy.SelectError:
		if timer_counter % 10 == 0:
			print "Nothing Found"
			timer_counter = 0
		pass
	timer_counter = timer_counter + 1
	time.sleep(.1)
