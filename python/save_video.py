# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 11:53:25 2015

@author: ajaver
"""
import subprocess as sp
import h5py
import matplotlib.pylab as plt
import time

maskFile = '/Volumes/ajaver$/GeckoVideo/Compressed/CaptureTest_90pc_Ch1_16022015_174636.hdf5';
saveVideo = '/Volumes/ajaver$/GeckoVideo/Compressed/CaptureTest_90pc_Ch1_16022015_174636.avi';
mask_fid = h5py.File(maskFile, "r");
data = mask_fid['/mask'];

print data.shape
#plt.imshow(data[0,:,:])


command = [ 'ffmpeg',
        '-y', # (optional) overwrite output file if it exists
        '-f', 'rawvideo',
        '-vcodec','rawvideo',
        '-s', '2048x2048', # size of one frame
        '-pix_fmt', 'gray',
        '-r', '50', # frames per second
        '-i', '-', # The imput comes from a pipe
        '-an', # Tells FFMPEG not to expect any audio
        '-vcodec', 'mjpeg',
        '-qscale:v', '0',
        '-vf', 'scale=512:512',
        saveVideo]

pipe = sp.Popen(command, stdin=sp.PIPE, stderr=sp.PIPE)

tic = time.time()
for frame_number in range(20):
    if frame_number%25 == 0:
            toc = time.time()
            print frame_number, toc-tic
            tic = toc
        
    pipe.stdin.write(data[frame_number+ 200000,:,:].tostring() )
plt.imshow(data[20,:,:], interpolation='none', cmap = 'gray')
pipe.terminate()

mask_fid.close()

