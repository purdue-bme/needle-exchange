import os
import glob
from time import sleep
from picamera import PiCamera


os.chdir('/home/pi/object_detection/training/input_images/')

# Prepare Name for File Save
list_of_files = glob.glob('/home/pi/object_detection/training/input_images/*.png')

camera = PiCamera()
camera.resolution = (1640, 922)
camera.start_preview()
# Camera warm-up time
sleep(0.2)

file_no = len(list_of_files)

capture_name = 'capture' + str(file_no+1) + '.jpeg'
print(capture_name)

# Turn the Camera On
camera.capture(capture_name, format="jpeg")
