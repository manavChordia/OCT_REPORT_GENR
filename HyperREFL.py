import numpy as np
import cv2

import matplotlib.pyplot as plt
import matplotlib.image as mpimg



frame =cv2.imread("IMG (17).jpg",1)

cv2.imshow("OCT",frame)
shp=frame.shape            # dimensions
print(shp[0])

hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)


# BLue
lower_color=np.array([90,80,90])        #hsv
upper_color=np.array([150,255,255])

mask=cv2.inRange(hsv,lower_color,upper_color)
res=cv2.bitwise_and(frame,frame,mask=mask)

cv2.imshow("Blue MASK",mask)
cv2.imshow("Result",res)

# REd
lower_color1=np.array([0,80,90])        #hsv
upper_color1=np.array([30,255,255])

maskr=cv2.inRange(hsv,lower_color1,upper_color1)
res1=cv2.bitwise_and(frame,frame,mask=maskr)

cv2.imshow("Red MASK",maskr)
cv2.imshow("red",res1)

#Green


lower_color2=np.array([40,80,90])        #hsv
upper_color2=np.array([80,255,255])

mask2=cv2.inRange(hsv,lower_color2,upper_color2)
res2=cv2.bitwise_and(frame,frame,mask=mask2)

inv_mask=cv2.bitwise_not(mask)
resinv=cv2.bitwise_and(frame,frame,mask=inv_mask)

cv2.imshow("Inverted blue mask",inv_mask)
cv2.imshow("Inverted blue ",resinv)


count =0

print(maskr[0][0])

for i in range(shp[0]-10) :
    j = 0
    for j in range(shp[1]):


        if (maskr[i][j]==255):     #on red mask if pixel is white
            maskr[i][j]=90
            print(i,j)
            resinv[i][j] = (55, 55, 55)
            for k in range(10):
                #print(resinv[i][j+k])
                a=resinv[i-k][j]     #blue to black mask
                #resinv[i-k][j] = (255, 255, 255)
                #print(a)
                if(a[0]==0 and a[1]==0 and a[2]==0):
                    resinv[i-k][j] = (255, 255, 255)
                    print(i,j-k)
                    count=count+1
                    print(i,j-k)


#plt.imshow(resinv)

print(count)

cv2.imshow("Green MASK",mask2)
cv2.imshow("green ",res2)
cv2.imshow("sd",resinv)
cv2.waitKey(0)
cv2.destroyAllWindows()





print(resinv.shape)
l=[]
r=[]

for i in range(resinv.shape[1]):

    if i>=90 and i<=160:  #GET THIS VALUE FROM ValueMAC PROGRAM
        continue
    else:
        for j in range(resinv.shape[0]):
            c = resinv[j][i]

            if c[0] == 0 and c[1] == 0 and c[2] == 0 or c[0] == 255 and c[1] == 255 and c[2] == 255:   #IF IT FINDS GREEN LAYER IT BREAKS FORM LOOP
                if i < resinv.shape[0] / 2:

                    if c[0] == 255 and c[1] == 255 and c[2] == 255:
                        l.append([i, j])
                        break
                else:

                    if c[0] == 255 and c[1] == 255 and c[2] == 255:
                        r.append([i, j])
                        break
            else:
                break

if len(l)>30:  #THIS IS ASSUMED THRESHOLD WORKS FOR NOTICABLE HYPER-REFLECTIVE
    print("HYPER-REFLECTIVE LAYER FOUND ON LEFT SIDE SCAN ABNORMAL")
if len(r)>30:
    print("HYPER-REFLECTIVE LAYER FOUND ON RIGHT SIDE SCAN ABNORMAL")
