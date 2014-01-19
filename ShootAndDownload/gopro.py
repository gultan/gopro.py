#!/usr/bin/python
#CHANGE X BY THE SECONDS BETWEEN THE LOOP.
#CHANGE WIFIPASSWORD BY THE GOPRO WIFI PASSORD
from time import sleep
import urllib2

while True:
time.sleep(X)
urllib2.urlopen ("http://10.5.5.9/bacpac/SH?t=WIFIPASSWORD&p=%01") 
time.sleep(3)
urllib.urlretrieve ("http://10.5.5.9:8080/videos/DCIM/100GOPRO/GOPR0001.JPG", "jpg.jpg")
time.sleep(6)
urllib2.urlopen ("http://10.5.5.9/camera/DA?t=WIFIPASSWORD")