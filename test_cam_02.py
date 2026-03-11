from picamera2 import Picamera2

# make cam object
picam2 = Picamera2()

# cam start 1mai satsuei
# 
picam2.start_and_capture_file("test.jpg")