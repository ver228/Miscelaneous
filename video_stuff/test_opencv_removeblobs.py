# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 18:22:50 2015

@author: ajaver
"""

tic = time.time();


IM_LIMX = image.shape[0]-2
IM_LIMY = image.shape[1]-2
MAX_AREA = 5000
MIN_AREA = 100
    
mask = cv2.adaptiveThreshold(image,1,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV,61,15)
[contours, hierrchy]= cv2.findContours(mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
badIndex = []
for ii, contour in enumerate(contours):
    if np.any(contour==1) or np.any(contour[:,:,0] ==  IM_LIMX)\
    or np.any(contour[:,:,1] == IM_LIMY):
        badIndex.append(ii) 
    else:
        area = cv2.contourArea(contour)
        if area<MIN_AREA or area>MAX_AREA:
            badIndex.append(ii)
for ii in badIndex:
    cv2.drawContours(mask, contours, ii, 0, cv2.cv.CV_FILLED)
mask[0,:] = 0; mask[:,0] = 0; mask[-1,:] = 0; mask[:,-1]=0;

mask = cv2.dilate(mask, STRUCT_ELEMENT, iterations = 3)
    
print time.time()-tic;

plt.figure()
plt.imshow(mask, interpolation='none', cmap = 'gray')

#tic = time.time();
#mask = cv2.adaptiveThreshold(image,1,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV,61,15)
#label_im, nb_labels = nd.label(mask);
#label_area = nd.sum(mask, label_im, range(nb_labels + 1))
#    #print 'NL %i' % nb_labels
#mask = np.bitwise_not(np.bitwise_or(label_area<100,label_area>5000))[label_im]
#print time.time()-tic;



#mask2 = nd.binary_erosion(mask2, nd.generate_binary_structure(2,2), iterations= 10,border_value=1);
    