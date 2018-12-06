"""
RPi.GPIO pins needed:
Pi GPIO 5 to keypad pin 1
Pi GPIO 6 to keypad pin 2
Pi GPIO 13 to keypad pin 3
Pi GPIO 19 to keypad pin 4
Pi GPIO 26 to keypad pin 5
Pi GPIO 16 to keypad pin 6
Pi GPIO 20 to keypad pin 7
Pi GPIO 21 to keypad pin 8
"""

# code suggested to access RPi GPIO pins:
# https://www.dummies.com/computers/raspberry-pi/use-python-access-gpio-pins-raspberry-pi/

# code suggested using CIrcuitPython installation of Matrix Keypad Library:
# https://learn.adafruit.com/matrix-keypad/python-circuitpython

#!/usr/bin/python3
import time
import digitalio
import RPi.GPIO as GPIO #import RPi.GPIO as GPIO
import adafruit_matrixkeypad as amk #import Adafruit Matrix Keypad Library as amk

5, 6, 13, 19, 26, 16, 20, 21

cols = [GPIO.setup(x,GPIO.IN) for x in (13, 5, 26)]
crows = [GPIO.setup(x,GPIO.IN) for x in (6, 21

"""
import time
import digitalio
import board
import adafruit_matrixkeypad

cols = [digitalio.DigitalInOut(x) for x in (board.D11, board.D13, board.D9)]
rows = [digitalio.DigitalInOut(x) for x in (board.D12, board.D5, board.D6, board.D10)]
keys = ((1, 2, 3, 'A'),
        (4, 5, 6, 'B'),
        (7, 8, 9, 'C'),
        ('*', 0, '#', 'D'))

keypad = adafruit_matrxikeypad.MatrixKeypad(rows, cols, keys)

while True:
  keys = keypad.presed_keys
  if keys:
    print("Press: ", keys)
    time.sleep(0.1)
"""
