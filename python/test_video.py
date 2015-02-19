# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 11:17:49 2015

@author: ajaver
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 13:33:18 2015

@author: ajaver
"""
import multiprocessing as mp
import cv2
#from functools import partial

import numpy as np
from skimage.measure import regionprops, label
from skimage import morphology
import Queue
import h5py
import tables
import time
import matplotlib.pylab as plt

N_processes = 24;


if __name__ == "__main__":   
#    fileName = '/Volumes/ajaver$/DinoLite/Videos/Exp5-20150116/A002 - 20150116_140923.wmv';    
#    bgndFile = '/Volumes/ajaver$/DinoLite/Results/Exp5-20150116-2/A002 - 20150116_140923.hdf5';
#    maskDB = '/Volumes/ajaver$/DinoLite/Results/Exp5-20150116-2/A002 - 20150116_140923_mask.db';
#    maskFile = '/Volumes/ajaver$/DinoLite/Results/Exp5-20150116-2/A002 - 20150116_140923_mask.hdf5';

    
    fileName = '/Volumes/ajaver$/DinoLite/Videos/Exp5-20150116/A002 - 20150116_140923.wmv';
    bgndFile = '/Volumes/ajaver$/DinoLite/Results/Exp5-20150116/A002 - 20150116_140923F.hdf5';
    featuresFile = '/Volumes/ajaver$/DinoLite/Results/Exp5-20150116/A002 - 20150116_140923D_features-2m.hdf5';
    maskFile = '/Volumes/ajaver$/DinoLite/Results/Exp5-20150116/A002 - 20150116_140923D_mask-2fn.hdf5';


#'''START TO READ THE HDF5 FROM THE PREVIOUSLY PROCESSED BGND '''    
    bgnd_fid = h5py.File(bgndFile, "r");
    bgnd = bgnd_fid["/bgnd"];
    BUFF_SIZE = bgnd.attrs['buffer_size'];
    BUFF_DELTA = bgnd.attrs['delta_btw_bgnd'];
    INITIAL_FRAME = bgnd.attrs['initial_frame'];


#'''OPEN THE VIDEO FILE AND EXTRACT SOME PARAMETERS'''        
    vid = cv2.VideoCapture(fileName)
    vid.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, INITIAL_FRAME);#initialize video to the initial position of the background buffer 
    im_width = vid.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
    im_height = vid.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)

    
#'''INITIALIZE VARIABLES'''   
    processes = Queue.Queue()
    max_frame = int(BUFF_DELTA*(bgnd.shape[0] + np.ceil(BUFF_SIZE/2)));
    max_frame = 3000;    
    nChunk_prev = -1;
    coord_prev = np.empty([0]);
    totWorms = 0;
    indexListPrev = np.empty([0]);
    results_list = [];
    meanI = np.zeros(max_frame);
    tic = time.time();
#'''MAIN LOOP STARTS'''   
    for ind_frame in range(max_frame):
        
        if ind_frame % 100 == 0:
            toc = time.time();
            print ind_frame, toc-tic;
            tic = toc;
            
            
        retval, image = vid.read()
        
        if not retval:
            break;
#        else:
#            meanI[ind_frame] = np.mean(image);
#   
    vid.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, INITIAL_FRAME);
    retval, image2 = vid.read()
    
    plt.figure()
    f, (ax1, ax2) = plt.subplots(1,2)
    ax1.imshow(image, interpolation = 'none', cmap = 'gray')
    ax2.imshow(image2, interpolation = 'none', cmap = 'gray')
        
    
    bgnd_fid.close()
    #mask_fid.close()
    #vid.release()
