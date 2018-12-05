import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)



user_database = open('./user_database.csv', 'r+')
i = 1

while True:
	keypad_input = input('Please enter a four-digit passcode: ')
	i += 1
	if i > 3:
		print('Access denied. Too many attempts.')
                break
	#if keypad_input.isdigit() == false:
	#	print('Passcode must be four numerical digits.')
	#else:
		if len(keypad_input) > 0:
			if len(keypad_input) == 4:
				for line in user_database:
					user_ID = line.split(",")
				if keypad_input in user_ID:
					print('Access granted.')
					line = user_database.writeline(l)
					break
				else:
                                        print('Acces denied. User not recognized.')
                        if len(keypad_input) > 4 or len(keypad_input) < 4:
                                print('Passcode must be four digits.')
                                keypad_input = []
