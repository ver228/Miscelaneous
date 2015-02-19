# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 19:44:17 2015

@author: ajaver
"""
from scipy.sparse import coo_matrix
import numpy as np


for nn in np.unique(II):
    #xx = shape.
    good = II == nn;
    t = TT[good];
    
    x = XX[good];
    y = YY[good];
    plt.plot(x,y, '.-')