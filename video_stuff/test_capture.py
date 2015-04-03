# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 15:37:27 2015

@author: ajaver
"""

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

fourcc = cv2.cv.CV_FOURCC(*'H264')
capSize = (720, 1280)
fps = 25;


#vout = cv2.VideoWriter();
#success = vout.open('output.mov',fourcc,fps,capSize,True) 


vout = cv2.VideoWriter();
success = vout.open('output.avi',fourcc,fps,capSize,True) 


for frame in range(100):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    vout.write(gray);
    # Display the resulting frame
    
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break

vout.release()
# When everything done, release the capture
#vout.release()
cap.release()
#cv2.destroyAllWindows()
