import cv2
import numpy as np
import imutils

image = cv2.imread("")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_red = np.array([160,20,70])
upper_red = np.array([190,255,255])

lower_yellow = np.array([25,70,120])
upper_yellow = np.array([30,255,255])

lower_blue = np.array([90,60,0])
upper_blue = np.array([121,255,255])

lower_green = np.array([40,70,80])
upper_green = np.array([70,255,255])

lower_white = np.array([211,211,211])
upper_white = np.array([255,255,255])

lower_orange = np.array([18, 40, 90])
upper_orange = np.array([27,255,255])

mask1 = cv2.inRange(hsv,lower_red,upper_red)
mask2 = cv2.inRange(hsv,lower_yellow,upper_yellow)
mask3 = cv2.inRange(hsv,lower_blue,upper_blue)
mask4 = cv2.inRange(hsv,lower_green,upper_green)
mask5 = cv2.inRange(hsv,lower_white,upper_white)
mask6 = cv2.inRange(hsv,lower_orange,upper_orange)

cnts1 = cv2.findContours(mask1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts1 = imutils.grab_contours(cnts1)

cnts2 = cv2.findContours(mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts2 = imutils.grab_contours(cnts2)

cnts3 = cv2.findContours(mask3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts3 = imutils.grab_contours(cnts3)

cnts4 = cv2.findContours(mask4, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts4 = imutils.grab_contours(cnts4)

cnts5 = cv2.findContours(mask5, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts5 = imutils.grab_contours(cnts5)

cnts6 = cv2.findContours(mask6, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts6 = imutils.grab_contours(cnts6)

for c in cnts1:
    area = cv2.contourArea(c)
    if area > 500:


        cv2.drawContours(image,[c],-1,(0,255,0), 3)

        M = cv2.moments(c)

        cx = int(M["m10"]/ M["m00"])
        cy = int(M["m01"]/ M["m00"])

        cv2.circle(image,(cx,cy),7,(255,255,255),-1)
        cv2.putText(image,"Red",(cx-20,cy-20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)

for c in cnts2:
    area = cv2.contourArea(c)
    if area > 500:


        cv2.drawContours(image,[c],-1,(0,255,0), 3)

        M = cv2.moments(c)

        cx = int(M["m10"]/ M["m00"])
        cy = int(M["m01"]/ M["m00"])

        cv2.circle(image,(cx,cy),7,(255,255,255),-1)
        cv2.putText(image,"Yellow",(cx-20,cy-20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)

for c in cnts3:
    area = cv2.contourArea(c)
    if area > 500:


        cv2.drawContours(image,[c],-1,(0,255,0), 3)

        M = cv2.moments(c)

        cx = int(M["m10"]/ M["m00"])
        cy = int(M["m01"]/ M["m00"])

        cv2.circle(image,(cx,cy),7,(255,255,255),-1)
        cv2.putText(image,"Blue",(cx-20,cy-20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)

for c in cnts4:
    area = cv2.contourArea(c)
    if area > 750:


        cv2.drawContours(image,[c],-1,(0,255,0), 3)

        M = cv2.moments(c)

        cx = int(M["m10"]/ M["m00"])
        cy = int(M["m01"]/ M["m00"])

        cv2.circle(image,(cx,cy),7,(255,255,255),-1)
        cv2.putText(image,"Green",(cx-20,cy-20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)

for c in cnts5:
    area = cv2.contourArea(c)
    if area > 500:


        cv2.drawContours(image,[c],-1,(0,255,0), 3)

        M = cv2.moments(c)

        cx = int(M["m10"]/ M["m00"])
        cy = int(M["m01"]/ M["m00"])

        cv2.circle(image,(cx,cy),7,(255,255,255),-1)
        cv2.putText(image,"White",(cx-20,cy-20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)

for c in cnts6:
    area = cv2.contourArea(c)
    if area > 500:


        cv2.drawContours(image,[c],-1,(0,255,0), 3)

        M = cv2.moments(c)

        cx = int(M["m10"]/ M["m00"])
        cy = int(M["m01"]/ M["m00"])

        cv2.circle(image,(cx,cy),7,(255,255,255),-1)
        cv2.putText(image,"Orange",(cx-20,cy-20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)

##cv2.imshow("result",image) 
##cv2.waitKey(0)

cv2.destroyAllWindows()
