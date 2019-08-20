# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 18:26:18 2019

@author: ManavChordia
"""

"""
Created on Thu Jul 11 18:30:51 2019
@author: manav
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('C:\\Users\\manav\\OCT2017\\OCT2017\\image_process\\IMG(104).jpg',1)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("macular_hole",img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()

_,thresh = cv2.threshold(img_gray, 120, 255, cv2.THRESH_BINARY)
cv2.imshow("macular_hole",thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()



lower_color=np.array([90,80,90])        #hsv
upper_color=np.array([150,255,255])

mask=cv2.inRange(img_hsv,lower_color,upper_color)
res=cv2.bitwise_and(img,img,mask=mask)

cv2.imshow("MASK",mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("Result",res)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(img, cmap='gray', interpolation='bicubic')

img[80][0]
l=[]
x=0
y=0
i=0
j=0
for i in range(1445):
    for j in range(1010):
        if (thresh[j+1][i]-thresh[j][i]) == 255:
            print("in if")
            print(i,j)
            l.append([i,j])
            break;
            
i1=0
j1=300
w=0
l1=[]
i=0
for i in range(1020):
    for w in range(990):
        if (thresh[j1-w-1][i]-thresh[j1-w][i]) == 255:
            print(i,j1-w)
            l1.append([i,j1-w])
            break;
        
for a in range(1011):
    if l[a+1][1]-l[a][1]>=40:
        print("Macular Hole")
        break