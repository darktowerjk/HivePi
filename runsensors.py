#!/usr/bin/python
import sys
import picamera
import time
from time import sleep
import RPi.GPIO as GPIO
import Adafruit_DHT
import httplib, urllib
from __future__ import print_function
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

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/drive.metadata.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'DriveAPI'

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'drive-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


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

    #Creates a Google Drive API service object and outputs the names and IDs
    #for up to 10 files.
    #"""
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v3', http=http)

    results = service.files().list(
        pageSize=10,fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])
    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print('{0} ({1})'.format(item['name'], item['id']))

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
