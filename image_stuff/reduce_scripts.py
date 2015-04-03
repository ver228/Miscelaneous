# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 16:39:42 2015

@author: ajaver
"""
import os
prefix = '/Users/ajaver/Desktop/20150126_Cam2_BMP/DCR_F_1065_';

iniIndex = 34987
for n in range(500):
    os.rename(prefix + str(iniIndex + n) + '.BMP', prefix + str(n+1) + '.BMP')  
