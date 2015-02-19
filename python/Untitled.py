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
fileName = '/Volumes/Mrc-pc/GeckoVideo/CaptureTest_90pc_Ch4_16022015_174636.mjpg';
FFMPEG_CMD = 'ffmpeg'


import numpy as np
import matplotlib.pylab as plt
import cv2
import subprocess as sp
import time
import os
command = [FFMPEG_CMD, 
           '-i', fileName,
           '-f', 'image2pipe',
           '-vcodec', 'rawvideo', '-']


pipe = sp.Popen(command, stdout = sp.PIPE, bufsize = 2048*2048) #use a buffer size as small as possible, makes things faster

tic = time.time()
tot_pix = 2048*2048



frame_number = 0;
tic = time.time()
while frame_number < 1:
    raw_image = pipe.stdout.read(tot_pix)
    
    if len(raw_image) < tot_pix:
        break;
    dum = raw_image
    frame_number += 1;
    image = np.fromstring(raw_image, dtype='uint8')
    image = image.reshape(2048,2048)

    if frame_number%25 == 1:
        toc = time.time()
        print frame_number, toc-tic
        tic = toc
    

#
pipe.stdout.flush()


mask = cv2.adaptiveThreshold(image,1,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,61,-10)

plt.figure()
plt.imshow(image, interpolation='none', cmap= 'gray')
plt.imshow(mask, interpolation='none', cmap= 'gray')


#vid = cv2.VideoCapture(filename)
#
#tic = time.time()
#tot_images = 0;
#while 1:#tot_frames < max_frames:
#    retval, image = vid.read()
#    if not retval:
#        break;
#print tot_images, time.time() - tic;

#image = np.fromstring(raw_image, dtype='uint8')
#image = image.reshape(2048,2048)
#plt.imshow(image)
