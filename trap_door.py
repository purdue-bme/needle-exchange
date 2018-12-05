# Servo Control

import RPi.GPIO as GPIO
import time

solenoid, servoPIN = 17, 22
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(servoPIN, GPIO.OUT)
GPIO.setup(solenoid, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization

try:
    GPIO.output(solenoid,GPIO.HIGH)
    p.ChangeDutyCycle(12.5)
    time.sleep(5)
    p.ChangeDutyCycle(2.5)
    time.sleep(1)
    GPIO.output(solenoid,GPIO.LOW)

except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
