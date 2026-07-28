import time
from picamera2 import Picamera2, Preview
from libcamera import Transform

picam = Picamera2()

config = picam.create_preview_configuration(main={"size": (2304, 1296)})
picam.configure(config)

picam.start_preview(Preview.QTGL, transform=Transform(hflip=0, vflip=1))

picam.start()
time.sleep(30000)

picam.close()