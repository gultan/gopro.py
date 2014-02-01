#!/usr/bin/python

#####################################################
#### NOTE: THIS SOFTWARE IS IN THE PUBLIC DOMAIN ####
#####################################################
"""
gopro.py by Konrad Iturbe, based on the work of Phill MacKay
"""

from urllib2 import urlopen
#import scipy as sp
#import cv2
from time import sleep

# Global variable. I know... I'm a bad programmer.
# After importing this module, you should do: goPro.password = "your real password"
password = "goprohero"

def initInteractive():
    # Interactive (test) mode. Comment out when importing inside a program.
    #If you're in python 3, change 'raw_input' by 'input'.
    password = raw_input("Enter your camera's wifi password (press Enter for default password)\n")
    if password == "": password = "goprohero"

def send(group,action):
    # Every command is pretty much the same...
    try:
        urlopen("http://10.5.5.9/camera/"+group+"?t="+password+"&p=%"+action, timeout=0.01)
    except:
        pass


def beep():
    send("LL","01")
    sleep(1)
    send("LL","00")


def powerOn():
    
    try:
        urlopen("http://10.5.5.9/bacpac/PW?t="+password+"&p=%01", timeout=1)
    except:
        pass

def powerOff():
    send("PW","00")

def startCapture():
    send("SH","01")

def stopCapture():
    send("SH","00")

def previewOn():
    send("PV","02")

def previewOff():
    send("PV","00")

def modeVideo():
    send("CM","00")

def modePhoto():
    send("CM","01")

def modeBurst():
    send("CM","02")

def modeTimelapse():
    send("CM","03")

def orientationUp():
    send("UP","00")

def orientationDown():
    send("UP","01")

def videoResolution4k():
    send("VR","02")


def proTuneOn():
    send("PT","01")

def proTuneOff():
    send("PT","00")


def fovWide():
    send("FV","00")

def fovMedium():
    send("FV","01")

def fovNarrow():
    send("FV","02")

def photoRes12Wide():
    send("PR","05")

def photoRes8Medium():
    send("PR","01")

def timelapse60sec():
    send("TI","06")

def locateOn():
    send("LL","01")

def locateOff():
    send("LL","00")

def beepMute():
    
    send("BS","00")
    
def beepLow():
    
    send("BS","01")

def beepHigh():
  
    send("BS","02")

def burstRate3in1():
  
    send("BU","00")

def burstRate10in1():
  
    send("BU","02")

def burstRate10in2():
  
    send("BU","03")

def burstRate30in1():
  
    send("BU","04")

def burstRate30in2():
  
    send("BU","05")

def burstRate30in3():
  
    send("BU","06")
