import time
import RPi.GPIO as GPIO

door = 23

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(door, GPIO.OUT)

GPIO.output(door,GPIO.HIGH)
time.sleep(5)
GPIO.output(m2,GPIO.LOW)
