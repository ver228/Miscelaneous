# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 16:44:30 2015

@author: ajaver
"""
import cv2
import time
import matplotlib.pylab as plt
import ndimage
from skimage.measure import regionprops, label
from skimage import morphology


fileName = '/Volumes/ajaver$/DinoLite/Videos/Exp5-20150116/A002 - 20150116_140923.wmv';
fileName = '/Volumes/Mrc-pc/GeckoVideo/CaptureTest_85pc_Ch1_13022015_163523.mjpg';
fileName = '/Volumes/Mrc-pc/GeckoVideo/CaptureTest_90pc_Ch3_16022015_171848.mjpg';


vid = cv2.VideoCapture(fileName)

tic_first = time.time()
tic = tic_first

max_frames = 10;
tot_frames = 0;
while tot_frames < max_frames:
    retval, image = vid.read()
    if not retval:
        break;
    tot_frames += 1;
    if tot_frames%10 == 1:
        toc = time.time()
        print tot_frames, toc-tic
        tic = toc
    
    
    
    
print tot_frames, time.time()- tic
image = cv2.cvtColor(image, cv2.cv.CV_RGB2GRAY);
mask = cv2.adaptiveThreshold(image,1,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,61,20)
L = label(mask)



plt.figure()
plt.imshow(mask2, cmap = 'gray', interpolation = 'none')
plt.figure()
plt.imshow(image, cmap = 'gray', interpolation = 'none')