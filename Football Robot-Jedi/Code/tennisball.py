#I HAVE NOT CALLED THIS FUNCTION IN THE MAIN ANYWHERE YET.




import numpy as np
import cv2
import motion as m
import urllib
from time import sleep
import servo as s
def findgoal(e1,e2):
        print("follow")
        url='http://192.168.43.33:8080/shot.jpg'
        f=-1;n=0;

        imgResp=urllib.urlopen(url)
        imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
        img=cv2.imdecode(imgNp,15000)
        print(img.shape)
        rows,cols,x = img.shape

        cv2.imshow('tracking',img)
        task="locate"
        f=0
        while True:
                listimg=None
                imgResp=urllib.urlopen(url)
                imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
                img=cv2.imdecode(imgNp,15000)
                hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
                lower_yellow=np.array([0,240,190])#tennis ball= fluorescent yellow = 0,255,204 (bgr)
                upper_yellow=np.array([5,255,215])
                masky=cv2.inRange(hsv,lower_yellow,upper_yellow)
                resy=cv2.bitwise_and(img,img,masky=masky)


                kernel=np.ones((5,5),np.uint8)

                openingy = cv2.morphologyEx(masky, cv2.MORPH_OPEN, kernel)
                closingy = cv2.morphologyEx(masky, cv2.MORPH_CLOSE, kernel)


                cv2.imshow('tracking',img)


                if(task=="locate"):
                                                        print("locaTE")

                                                        circles=cv2.HoughCircles(closingy,cv2.HOUGH_GRADIENT,2,120,param1=50,param2=25,minRadius=10,maxRadius$
                                                        print(circles)
                                                        if circles is not None:
                                                          listimg=circles[0,:]

                                                          print("listimg")
                                                          print(listimg)
                                                          task="turn"


                                                        else:
                                                                if f%3!=0:
                                                                    pass
                                                                print("clockwise")
                                                                m.clockwise(30,e2)
                                                                sleep(2)




                if (task=="turn"):
                                                        print("TURN")

                                                        circles=cv2.HoughCircles(closingy,cv2.HOUGH_GRADIENT,2,120,param1=60,param2=30,minRadius=10,maxRadius$
                                                        if circles is not None:
                                                                        listimg=circles[0,:]

                                                                        i=listimg[0]
                                                                        print("coord")
                                                                        print(i)
                                                                        cv2.circle(img,(int(round(i[0])),int(round(i[1]))),int(round(i[2])),(255,0,0),4)
                                                                        cv2.circle(img,(int(round(i[0])),int(round(i[1]))),1,(0,255,0),4)



                                                                        err=cols/20
                                                                        print ((cols/2)-err/2)
                                                                        if(i[0]<(cols/2)-err/2 or i[0]>(cols/2)+err/2):



                                                                                if(i[0]>cols/2):
                                                                                    if(i[0]-cols/2>=4*err):
                                                                                        m.clockwise(2*40*(i[0]-cols/2)/cols,e2)
                                                                                        print("turning right")
                                                                                    elif(i[0]-cols/2<=1*err):
                                                                                        m.clockwise(3,e2)
                                                                                        print("turning right")
                                                                                    else:
                                                                                        m.clockwise(2*15*(i[0]-cols/2)/cols,e2)
                                                                                        print("turning right")



                                                                                if(i[0]<cols/2):
                                                                                    if(i[0]-cols/2<=4*err):
                                                                                        m.anticlockwise(2*40*-1*(i[0]-cols/2)/cols,e2)
                                                                                        print("turning left")
                                                                                    elif(i[0]-cols/2>=1*err):
                                                                                        m.anticlockwise(3,e2)
                                                                                        print("turning left")
                                                                                    else:
                                                                                        m.anticlockwise(15*2*-1*(i[0]-cols/2)/cols,e2)
                                                                                        print("turning left")
                                                                        else:

                                                                           task="forward"
                                                        else :
                                                                task="locate"
                                                                f+=1
                if (task=="forward"):
                                print("forward")

                                circles=cv2.HoughCircles(closingy,cv2.HOUGH_GRADIENT,2,120,param1=75,param2=35,minRadius=10,maxRadius=100) #MIGHT HAVE TO CHANGE MIN AND MAX SINCE TENNIS BALL IS BIG
                                if circles is not None:

                                   listimg=circles[0,:]


                                   if (True):
                                                                        i=listimg[0]
                                                                        print("coord")
                                                                        print(i)
                                                                        cv2.circle(img,(int(round(i[0])),int(round(i[1]))),int(round(i[2])),(255,0,0),4)
                                                                        cv2.circle(img,(int(round(i[0])),int(round(i[1]))),1,(0,255,0),4)

                                                                        if(i[2]<200): #again may need change of threshold due to size of ball
                                                                            if(i[2]<50):
                                                                                m.forward(30,e1)
                                                                                print("going ahead")
                                                                                sf=1
                                                                            if (i[2]<100):
                                                                                m.forward(15,e1)
                                                                                print("going ahead")
                                                                                sf=1
                                                                            else:
                                                                                m.forward(15,e1)
                                                                                print("going ahead")
                                                                                sf=1
                                                                        else:
                                                                                task="locate"
                                                                                f=0
                                                                                break
                                else:
                                            task="locate"
                                            f+=1




                k = cv2.waitKey(5) & 0xFF
                if k == 27:

                  cv2.destroyAllWindows()
                  break;


