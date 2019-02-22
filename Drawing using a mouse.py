import cv2
import numpy as np
import pandas as pd


def draw_circle(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:#left button clicked down
        cv2.circle(img,(x,y),100,(0,255,0),-1)
    elif event==cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),100,(255,0,0),-1)        
        

cv2.namedWindow('my_drawing')#create window
cv2.setMouseCallback('my_drawing',draw_circle)


img=np.zeros((512,512,3),np.int8)#int8 makes the background a little more gray
#if I remove int8, the image will come out black

while True:
    cv2.imshow('my_drawing',img)
    
    if cv2.waitKey(20) & 0xFF==27:#wait for 20 miliseconds
        break
            
cv2.destroyAllWindows()


    

