# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 16:17:45 2015

@author: ajaver
"""
mainDir = '/Users/ajaver/Desktop/20150126_Cam2_BMP/';

import scipy.misc as smisc
#import matplotlib.pyplot as plt
import numpy as np
import struct
from skimage.io._plugins import freeimage_plugin as fi

import os 

fileList = os.listdir(mainDir)

fileList = [mainDir + x for x in fileList if 'BMP' in x ]
        
for filename in fileList:
    I = smisc.imread(filename)[:,:,0] #change rgb to gray
    smisc.imsave(filename,I)
