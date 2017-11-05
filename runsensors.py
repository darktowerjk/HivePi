#!/usr/bin/python
from __future__ import print_function
import sys
import picamera
import time
from time import sleep
import RPi.GPIO as GPIO
import Adafruit_DHT
import httplib, urllib
import httplib2
import os


from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

camera = picamera.PiCamera()
camera.capture('image.jpg')
delaytime=10;
key='UT38DSROKCUUHSOX'
DEBUG = 1




while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    print( 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity))
    params = urllib.urlencode({'field1': temperature, 'field2': humidity, 'key': key})
    headers = {"Content-typZZe": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    # store data in ThingSpeak
    conn = httplib.HTTPConnection("api.thingspeak.com:80")
    conn.request("POST", "/update", params, headers)
    response = conn.getresponse()
    print(response.status, response.reason)
    data = response.read()
    conn.close()


    time.sleep(delaytime);
if __name__ == '__main__':
    main()

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
