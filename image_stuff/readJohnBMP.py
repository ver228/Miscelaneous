# -*- coding: utf-8 -*-
"""
Created on Sat Jan 24 12:07:42 2015

@author: ajaver
"""

import scipy.misc as smisc
#import matplotlib.pyplot as plt
import numpy as np
import struct
from skimage.io._plugins import freeimage_plugin as fi

import os 

saveDir = '/Users/ajaver/Desktop/test_formats/';
bmpDir = saveDir + 'BMP/'

if not os.path.isdir(saveDir):
    os.mkdir(saveDir)
    os.mkdir(bmpDir)
elif not os.path.isdir(bmpDir):
    os.mkdir(bmpDir)


chunk = 56;
frameIni = 16449;
NImages = 450;

I = np.zeros((NImages, 2048,2048), dtype = np.uint8)
for nn in range(NImages):
    filename = '/Users/ajaver/Desktop/DCR_D_56/DCR_D_%i_%i.BMP' % (chunk, nn +frameIni)
    I[nn,:,:] = smisc.imread(filename)[:,:,0] #change rgb to gray
    #plt.figure()
    #plt.imshow(I[:,:,nn])


fi.write_multipage(I, saveDir + 'Tiff_LZW.tiff', fi.IO_FLAGS.TIFF_LZW)
fi.write_multipage(I, saveDir + 'Tiff_Uncompressed.tiff', fi.IO_FLAGS.TIFF_NONE)

for nn in range(I.shape[0]):
    fi.write(I[nn,:,:], bmpDir + '%03i.bmp' % nn)


# Change John's BMP into index-value arrays

FID = open (saveDir + 'reduced_indexes', "wb")

# Find list of indexes and pixel values
for nn in range(I.shape[0]):
    Isingle = I[nn,:,:]
    mask = (Isingle!=200) & (Isingle!=0)
    indexList = np.where(mask)
    valuesList = Isingle[indexList];
    #
    ##to save data into a binary file it is necessary to parse the data first into a valid enconde string format (struck module).
    Ndata = valuesList.size
    
    #header
    str_buff = struct.pack('HHIII', Isingle.shape[0], I.shape[1], chunk, nn +frameIni, Ndata)
    #indexes
    str_buff += struct.pack( '%iH' % Ndata, *indexList[0]);
    str_buff += struct.pack( '%iH' % Ndata, *indexList[0]);
    #pixel values
    str_buff += struct.pack( '%iB' % Ndata, *valuesList);
    FID.write(str_buff)

FID.close()

#
##save for the whole image
with open(saveDir + 'raw_data', "wb") as FID:
    I.tofile(FID)

#str_data = struct.pack('%iB' % I.size, *np.ravel(I))

