#!/usr/bin/python
import sys
import picamera
from time import sleep
import RPi.GPIO as GPIO
import Adafruit_DHT

camera = picamera.PiCamera()
camera.capture('image.jpg')


while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    TWF = ({0:0.1f} * 9 / 5) + 32
    temp =(str(TWF))
    print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
    print temp
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
