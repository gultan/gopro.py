{\rtf1\ansi\ansicpg1252\cocoartf1265
{\fonttbl\f0\fmodern\fcharset0 Courier-Oblique;\f1\fmodern\fcharset0 Courier;\f2\fmodern\fcharset0 Courier-Bold;
}
{\colortbl;\red255\green255\blue255;\red135\green136\blue117;\red38\green38\blue38;\red210\green0\blue53;
\red67\green67\blue67;\red133\green0\blue2;\red14\green114\blue164;\red17\green137\blue135;}
{\info
{\author KonradIT}
{\*\company HERO}
{\*\copyright 2012 QUE TE METO!}}\paperw11900\paperh16840\margl1440\margr1440\vieww11200\viewh10720\viewkind0
\deftab720
\pard\pardeftab720

\f0\i\fs24 \cf2 #!/usr/bin/python
\f1\i0 \cf3 \
\

\f0\i \cf2 #####################################################
\f1\i0 \cf3 \

\f0\i \cf2 #### NOTE: THIS SOFTWARE IS IN THE PUBLIC DOMAIN ####
\f1\i0 \cf3 \

\f0\i \cf2 #####################################################
\f1\i0 \cf3 \
\pard\pardeftab720
\cf4 """\cf3 \
\cf4 Go.Py by Konrad Iturbe, based on the work of Phill MacKay\cf3 \
\cf4 """\cf3 \
\
\pard\pardeftab720

\f2\b \cf3 from
\f1\b0 \cf3  \cf5 urllib2\cf3  
\f2\b \cf3 import
\f1\b0 \cf3  urlopen\
\pard\pardeftab720

\f0\i \cf2 #import scipy as sp
\f1\i0 \cf3 \

\f0\i \cf2 #import cv2
\f1\i0 \cf3 \
\pard\pardeftab720

\f2\b \cf3 from
\f1\b0 \cf3  \cf5 time\cf3  
\f2\b \cf3 import
\f1\b0 \cf3  sleep\
\
\pard\pardeftab720

\f0\i \cf2 # Global variable. I know... I'm a bad programmer.
\f1\i0 \cf3 \

\f0\i \cf2 # After importing this module, you should do: goPro.password = "your real password"
\f1\i0 \cf3 \
password 
\f2\b \cf3 =
\f1\b0 \cf3  \cf4 "goprohero"\cf3 \
\
\pard\pardeftab720

\f2\b \cf3 def
\f1\b0 \cf3  
\f2\b \cf6 initInteractive
\f1\b0 \cf3 ():\
\'a0\'a0\'a0\'a0
\f0\i \cf2 # Interactive (test) mode. Comment out when importing inside a program.
\f1\i0 \cf3 \
\'a0\'a0\'a0\'a0
\f0\i \cf2 #If you're in python 3, change 'raw_input' by 'input'.
\f1\i0 \cf3 \
\'a0\'a0\'a0\'a0password 
\f2\b \cf3 =
\f1\b0 \cf3  \cf7 raw_input\cf3 (\cf4 "Enter your camera's wifi password (press Enter for default password)\\n"\cf3 )\
\'a0\'a0\'a0\'a0
\f2\b \cf3 if
\f1\b0 \cf3  password 
\f2\b \cf3 ==
\f1\b0 \cf3  \cf4 ""\cf3 : password 
\f2\b \cf3 =
\f1\b0 \cf3  \cf4 "goprohero"\cf3 \
\

\f2\b \cf3 def
\f1\b0 \cf3  
\f2\b \cf6 send
\f1\b0 \cf3 (group,action):\
\'a0\'a0\'a0\'a0
\f0\i \cf2 # Every command is pretty much the same...
\f1\i0 \cf3 \
\'a0\'a0\'a0\'a0
\f2\b \cf3 try
\f1\b0 \cf3 :\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0urlopen(\cf4 "http://10.5.5.9/camera/"
\f2\b \cf3 +
\f1\b0 \cf3 group
\f2\b \cf3 +
\f1\b0 \cf4 "?t="
\f2\b \cf3 +
\f1\b0 \cf3 password
\f2\b \cf3 +
\f1\b0 \cf4 "&p=%"
\f2\b \cf3 +
\f1\b0 \cf3 action, timeout
\f2\b \cf3 =
\f1\b0 \cf8 0.01\cf3 )\
\'a0\'a0\'a0\'a0
\f2\b \cf3 except
\f1\b0 \cf3 :\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f2\b \cf3 pass
\f1\b0 \cf3 \
\
\

\f2\b \cf3 def
\f1\b0 \cf3  
\f2\b \cf6 beep
\f1\b0 \cf3 ():\
\'a0\'a0\'a0\'a0send(\cf4 "LL"\cf3 ,\cf4 "01"\cf3 )\
\'a0\'a0\'a0\'a0sleep(\cf8 1\cf3 )\
\'a0\'a0\'a0\'a0send(\cf4 "LL"\cf3 ,\cf4 "00"\cf3 )\
\
\

\f2\b \cf3 def
\f1\b0 \cf3  
\f2\b \cf6 powerOn
\f1\b0 \cf3 ():\
\'a0\'a0\'a0\'a0\
\'a0\'a0\'a0\'a0
\f2\b \cf3 try
\f1\b0 \cf3 :\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0urlopen(\cf4 "http://10.5.5.9/bacpac/PW?t="
\f2\b \cf3 +
\f1\b0 \cf3 password
\f2\b \cf3 +
\f1\b0 \cf4 "&p=%01"\cf3 , timeout
\f2\b \cf3 =
\f1\b0 \cf8 1\cf3 )\
\'a0\'a0\'a0\'a0
\f2\b \cf3 except
\f1\b0 \cf3 :\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f2\b \cf3 pass
\f1\b0 \cf3 \
\

\f2\b \cf3 def
\f1\b0 \cf3  
\f2\b \cf6 powerOff
\f1\b0 \cf3 ():\
\'a0\'a0\'a0\'a0send(\cf4 "PW"\cf3 ,\cf4 "00"\cf3 )\
\

\f2\b \cf3 def
\f1\b0 \cf3  
\f2\b \cf6 startCapture
\f1\b0 \cf3 ():\
\'a0\'a0\'a0\'a0send(\cf4 "SH"\cf3 ,\cf4 "01"\cf3 )\
\

\f2\b \cf3 def
\f1\b0 \cf3  
\f2\b \cf6 stopCapture
\f1\b0 \cf3 ():\
\'a0\'a0\'a0\'a0send(\cf4 "SH"\cf3 ,\cf4 "00"\cf3 )\
\

\f2\b \cf3 def
\f1\b0 \cf3  
\f2\b \cf6 previewOn
\f1\b0 \cf3 ():\
\'a0\'a0\'a0\'a0send(\cf4 "PV"\cf3 ,\cf4 "02"\cf3 )\
\

\f2\b \cf3 def
\f1\b0 \cf3  
\f2\b \cf6 previewOff
\f1\b0 \cf3 ():\
\'a0\'a0\'a0\'a0send(\cf4 "PV"\cf3 ,\cf4 "00"\cf3 )\
\

\f2\b \cf3 def
\f1\b0 \cf3  
\f2\b \cf6 modeVideo
\f1\b0 \cf3 ():\
\'a0\'a0\'a0\'a0send(\cf4 "CM"\cf3 ,\cf4 "00"\cf3 )\
\

\f2\b \cf3 def
\f1\b0 \cf3  
\f2\b \cf6 modePhoto
\f1\b0 \cf3 ():\
\'a0\'a0\'a0\'a0send(\cf4 "CM"\cf3 ,\cf4 "01"\cf3 )\
\

\f2\b \cf3 def
\f1\b0 \cf3  
\f2\b \cf6 modeBurst
\f1\b0 \cf3 ():\
\'a0\'a0\'a0\'a0send(\cf4 "CM"\cf3 ,\cf4 "02"\cf3 )\
\

\f2\b \cf3 def
\f1\b0 \cf3  
\f2\b \cf6 modeTimelapse
\f1\b0 \cf3 ():\
\'a0\'a0\'a0\'a0send(\cf4 "CM"\cf3 ,\cf4 "03"\cf3 )\
\

\f2\b \cf3 def
\f1\b0 \cf3  
\f2\b \cf6 orientationUp
\f1\b0 \cf3 ():\
\'a0\'a0\'a0\'a0send(\cf4 "UP"\cf3 ,\cf4 "00"\cf3 )\
\

\f2\b \cf3 def
\f1\b0 \cf3  
\f2\b \cf6 orientationDown
\f1\b0 \cf3 ():\
\'a0\'a0\'a0\'a0send(\cf4 "UP"\cf3 ,\cf4 "01"\cf3 )\
\

\f2\b \cf3 def
\f1\b0 \cf3  
\f2\b \cf6 videoResolution4k
\f1\b0 \cf3 ():\
\'a0\'a0\'a0\'a0send(\cf4 "VR"\cf3 ,\cf4 "02"\cf3 )\
\
\

\f2\b \cf3 def
\f1\b0 \cf3  
\f2\b \cf6 proTuneOn
\f1\b0 \cf3 ():\
\'a0\'a0\'a0\'a0send(\cf4 "PT"\cf3 ,\cf4 "01"\cf3 )\
\

\f2\b \cf3 def
\f1\b0 \cf3  
\f2\b \cf6 proTuneOff
\f1\b0 \cf3 ():\
\'a0\'a0\'a0\'a0send(\cf4 "PT"\cf3 ,\cf4 "00"\cf3 )\
\
\

\f2\b \cf3 def
\f1\b0 \cf3  
\f2\b \cf6 fovWide
\f1\b0 \cf3 ():\
\'a0\'a0\'a0\'a0send(\cf4 "FV"\cf3 ,\cf4 "00"\cf3 )\
\

\f2\b \cf3 def
\f1\b0 \cf3  
\f2\b \cf6 fovMedium
\f1\b0 \cf3 ():\
\'a0\'a0\'a0\'a0send(\cf4 "FV"\cf3 ,\cf4 "01"\cf3 )\
\

\f2\b \cf3 def
\f1\b0 \cf3  
\f2\b \cf6 fovNarrow
\f1\b0 \cf3 ():\
\'a0\'a0\'a0\'a0send(\cf4 "FV"\cf3 ,\cf4 "02"\cf3 )\
\

\f2\b \cf3 def
\f1\b0 \cf3  
\f2\b \cf6 photoRes12Wide
\f1\b0 \cf3 ():\
\'a0\'a0\'a0\'a0send(\cf4 "PR"\cf3 ,\cf4 "05"\cf3 )\
\

\f2\b \cf3 def
\f1\b0 \cf3  
\f2\b \cf6 photoRes8Medium
\f1\b0 \cf3 ():\
\'a0\'a0\'a0\'a0send(\cf4 "PR"\cf3 ,\cf4 "01"\cf3 )\
\

\f2\b \cf3 def
\f1\b0 \cf3  
\f2\b \cf6 timelapse60sec
\f1\b0 \cf3 ():\
\'a0\'a0\'a0\'a0send(\cf4 "TI"\cf3 ,\cf4 "06"\cf3 )\
\

\f2\b \cf3 def
\f1\b0 \cf3  
\f2\b \cf6 locateOn
\f1\b0 \cf3 ():\
\'a0\'a0\'a0\'a0send(\cf4 "LL"\cf3 ,\cf4 "01"\cf3 )\
\

\f2\b \cf3 def
\f1\b0 \cf3  
\f2\b \cf6 locateOff
\f1\b0 \cf3 ():\
\'a0\'a0\'a0\'a0send(\cf4 "LL"\cf3 ,\cf4 "00"\cf3 )\
\

\f2\b \cf3 def
\f1\b0 \cf3  
\f2\b \cf6 beepMute
\f1\b0 \cf3 ():\
\'a0\'a0\'a0\'a0\
\'a0\'a0\'a0\'a0send(\cf4 "BS"\cf3 ,\cf4 "00"\cf3 )\
\'a0\'a0\'a0\'a0\

\f2\b \cf3 def
\f1\b0 \cf3  
\f2\b \cf6 beepLow
\f1\b0 \cf3 ():\
\'a0\'a0\'a0\'a0\
\'a0\'a0\'a0\'a0send(\cf4 "BS"\cf3 ,\cf4 "01"\cf3 )\
\

\f2\b \cf3 def
\f1\b0 \cf3  
\f2\b \cf6 beepHigh
\f1\b0 \cf3 ():\
\'a0\'a0\
\'a0\'a0\'a0\'a0send(\cf4 "BS"\cf3 ,\cf4 "02"\cf3 )}