import picamera
from time import sleep
import RPi.GPIO as GPIO
import Adafruit_DHT

camera = picamera.PiCamera()
camera.capture('image.jpg')

RCpin = 24
DHTpin = 23

# Get Temp and Humidity
GPIO.setmode(GPIO.BCM)
GPIO.setup(RCpin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
RHW, TW = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, DHTpin)
# Convert from Celius to Farenheit
TWF = (TW * 9 / 5) + 32
temp =(str(TWF))
print temp
print TWF

# camera.hflip = True
# camera.vflip = True
#
# camera.start_preview()
# camera.stop_preview()
# camera.sharpness = 0
# camera.contrast = 0
# camera.brightness = 50
# camera.saturation = 0
# camera.ISO = 0
# camera.video_stabilization = False
# camera.exposure_compensation = 0
# camera.exposure_mode = 'auto'
# camera.meter_mode = 'average'
# camera.awb_mode = 'auto'
# camera.image_effect = 'none'
# camera.color_effects = None
# camera.rotation = 0
# camera.hflip = False
# camera.vflip = False
# camera.crop = (0.0, 0.0, 1.0, 1.0)
#
# # take a picture every 5 seconds
#
# camera = picamera.PiCamera()
#
# camera.capture('image1.jpg')
# sleep(5)
# camera.capture('image2.jpg')
#
# # record 5 seconds of video
# camera.start_recording('video.h264')
# sleep(5)
# camera.stop_recording()
