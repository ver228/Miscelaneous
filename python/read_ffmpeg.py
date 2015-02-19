# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 15:17:44 2015

@author: Avelino
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 15:06:13 2015

@author: ajaver
"""
#filename = '/Volumes/Mrc-pc/GeckoVideo/CaptureTest_90pc_Ch2_16022015_174636.mjpg';
FFMPEG_CMD = 'ffmpeg'

filename = '/Volumes/H/GeckoVideo/CaptureTest_85pc_Ch3_13022015_154646.mjpg'
#filename = 'H:\\GeckoVideo\\CaptureTest_85pc_Ch3_13022015_154646.mjpg'

import numpy as np
import matplotlib.pylab as plt
import cv2
import subprocess as sp
import time
import os
command = [FFMPEG_CMD, 
           '-i', filename,
           '-f', 'image2pipe',
           '-vcodec', 'rawvideo', '-']


pipe = sp.Popen(command, stdout = sp.PIPE, bufsize = 2048*2048) #use a buffer size as small as possible, makes things faster

tic = time.time()
tot_pix = 2048*2048



tot_images = 0;
while 1:
    raw_image = pipe.stdout.read(tot_pix)
    
    if len(raw_image) < tot_pix:
        break;
    dum = raw_image
    tot_images += 1;
    image = np.fromstring(raw_image, dtype='uint8')
    image = image.reshape(2048,2048)
    

print tot_images, time.time() - tic;
#
pipe.stdout.flush()


vid = cv2.VideoCapture(filename)

tic = time.time()
tot_images = 0;
while 1:
    retval, image = vid.read()
    if not retval:
        break;
    tot_images += 1
    
print tot_images, time.time() - tic;

#image = np.fromstring(raw_image, dtype='uint8')
#image = image.reshape(2048,2048)
#plt.imshow(image)
