# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 18:22:50 2015

@author: ajaver
"""

tic = time.time();
mask = cv2.adaptiveThreshold(image,1,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV,61,15)
[contours, hierarchy]= cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
for ii, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if area<100 or area>5000:
        cv2.drawContours(mask_dum, contours, ii, 0, cv2.cv.CV_FILLED)
print time.time()-tic;

tic = time.time();
mask = cv2.adaptiveThreshold(image,1,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV,61,15)
label_im, nb_labels = nd.label(mask);
label_area = nd.sum(mask, label_im, range(nb_labels + 1))
    #print 'NL %i' % nb_labels
mask = np.bitwise_not(np.bitwise_or(label_area<100,label_area>5000))[label_im]
print time.time()-tic;



#mask2 = nd.binary_erosion(mask2, nd.generate_binary_structure(2,2), iterations= 10,border_value=1);
    