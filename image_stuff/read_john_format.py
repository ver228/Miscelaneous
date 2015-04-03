# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 11:18:29 2015

@author: ajaver
"""
#from scipy import misc
#import matplotlib.pyplot as plt
import struct
import numpy as np

mainDir = '/Users/ajaver/Desktop/John_Format/';
image_shape = (2048,2048)
image_size = image_shape[0]*image_shape[1];
#bmp_prefix = mainDir + 'BMP/DCR_D_1237_';
#bmp_ini = 73227;
#I = misc.imread('%s%i.BMP' % (bmp_prefix, bmp_ini))[:,:,0]




#read all the file as a "bit-string"
with open(mainDir + 'DCR_D_1237.PVSeq', 'rb') as f:
    data = f.read()


tot = 0;
#start reading the file. It must start with PV01
iniBlock = data.find('PV01')
Ibuff = []
while iniBlock < len(data):
    tot += 1    
    print tot    
    
    #find the position of the next block of data using PV1, if not found set it to the lenght of the file 
    nextBlock = data.find('PV01', iniBlock+1)
    if nextBlock == -1:
        nextBlock == len(data) + 1;
    
    #I suspect the header is fix to a 2048 bytes length. Therefore the image data must be
    #between the initial data block shifted 2048, and the next data block
    compressed = data[iniBlock + 2048:nextBlock];
    
    #The image is compressed by anotated a continous set of zeros as (0, X,Y) where X, Y is a uint16 in big-endian notation
    #data is compompressed by remplacing the triplet with a segment of zeros.
    uncompressed = '';
    index_prev = 0;
    while 1:
        #find zeros
        index_new = compressed.find('\x00', index_prev)
        if index_new != -1:
            #find the number of zeros and remplace it with a bit-string of zeros
            num_rep = struct.unpack('>H', compressed[index_new+1:index_new+3])[0] ;
            uncompressed += compressed[index_prev:index_new] + (num_rep*'\x00')
            index_prev = index_new+3;
            
        else:
            #copy the rest of the data and exit if not zero is found
            uncompressed += compressed[index_prev:]
            break;
    
    #if there is still space to complete the image pad with zeros
    uncompressed += (image_size-len(uncompressed))*'\x00'
    
    #convert into a numpy array of the proper image size
    I = np.array(struct.unpack('%iB' % len(uncompressed), uncompressed)).reshape(image_shape);
    Ibuff.append(I);
        
    iniBlock = nextBlock;




#seg = struct.pack('BBB', 8,7,8)
#seg = struct.pack('BBB', 0,7,16)
#seg= struct.pack()
#
#ind_prev = -1.0;
#A = np.zeros(100)
#for m in range(A.size):
#    ind = dd.find(seg, int(ind_prev+1))
#    A[m] = ind
#    ind_prev = ind
#
#seg = struct.pack('I', 73226)






