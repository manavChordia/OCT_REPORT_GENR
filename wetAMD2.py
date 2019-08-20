
"""
Created on Sun Aug 11 16:22:46 2019

@author: ManavChordia
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 14:08:00 2019

@author: ManavChordia
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread('C:\\Users\\ManavChordia\\NIO\\IMG(95).jpg',1)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("wet_amd",img_hsv)

cv2.waitKey(0)
cv2.destroyAllWindows()

# REd
lower_color1=np.array([0,80,90])        #hsv
upper_color1=np.array([30,255,255])

maskr=cv2.inRange(img_hsv,lower_color1,upper_color1)
res1=cv2.bitwise_and(img,img,mask=maskr)

cv2.imshow("Red MASK",maskr)
#cv2.imshow("red",res1)

cv2.waitKey(0)
cv2.destroyAllWindows()

height = maskr.shape[0];
width = maskr.shape[1];

l=[]
lavg = []

for i in range(width):
    sum=0
    count=0
    for j in range(height):
        if maskr[j][i] == 255:
            sum = sum + j
            count=count+1
            l.append([i,j])
        else:
            continue
    if count != 0:
        lavg.append([i,sum//count])
    else:
        print(i)
    
for i in lavg:
    img[i[1]][i[0]] = (0,0,0)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

xavg=0
yavg=0
for i in lavg:
    xavg = xavg+i[0]
    yavg = yavg+i[1]
    
xavg = xavg//len(lavg)
yavg = yavg//len(lavg)


mx = 0
my = 0
for i in lavg:
    mx = mx + (xavg-i[0])*(yavg-i[1])
    my = my + (xavg-i[0])*(xavg-i[0])
    
m = mx/my
    
yintercept = yavg - m*xavg
yintercept = int(yintercept)
"""
cv2.line(img,(0,yintercept),(xavg,yavg),(0,0,0),2)
cv2.imshow("img",img)
cv2.waitKey(0)"""

yend = width*m + yintercept
yend = int(yend)
cv2.line(img,(0,yintercept),(width-1,yend),(0,0,0),2)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

import math

def distance(mx,my,c,x1,y1):
    return abs(my*y1-mx*x1-my*c)/(math.sqrt((my*my)+(mx*mx)))

dist = []
for i in lavg:
    x = distance(mx,my,yintercept,i[0],i[1])
    dist.append(x)

excess = 0

for i in dist:
    if i>=40:
        excess=excess+1
        
print(excess)

if excess > 20:
    print("wet amd present")
else:
    print("not present")
    
    


