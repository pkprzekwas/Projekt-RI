import matplotlib as plt
from shapely.geometry import LineString
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np

size=(320,240)

def startCamera():
        camera = PiCamera()
        camera.resolution = size
        return camera

def getFrameFromCamera(camera, show = False):
        rawCapture = PiRGBArray(camera, size=size)
        # allow the camera to warmup
        time.sleep(0.1)
        # grab an image from the camera
        camera.capture(rawCapture, format="bgr")
        image = rawCapture.array
        # display the image on screen and wait for a keypress
        if show:
            cv2.imshow("Image", image)
            cv2.waitKey(0)
        return image

def findDirectionError(img, show = False):
        #height, width = img.shape[:2]
        #img = cv2.resize(img,(int(0.5*width), int(0.5*height)), interpolation = cv2.INTER_CUBIC)
        height, width = img.shape[:2]
        img = img[height/2 : height, 0 : width]
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        gauss = cv2.GaussianBlur(gray,(3,3),0)
        edges = cv2.Canny(gray,0,140,apertureSize = 3)
        lines = cv2.HoughLines(edges,1,np.pi/180,50)
        lineList1=[]
        lineList2=[]
        try:
            for rho,theta in lines[0]:

                if len(lineList1) > 20 or len(lineList2) > 20:
                    break
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a*rho
                y0 = b*rho
                x1 = int(x0 + 1000*(-b))
                y1 = int(y0 + 1000*(a))
                x2 = int(x0 - 1000*(-b))
                y2 = int(y0 - 1000*(a))
                if abs(b) < 0.05 or abs(b) > 0.985 :
                    cv2.line(img,(x1,y1),(x2,y2),(0,0,0),1)
                    continue
                if theta >1.57:
                    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),1)
                    lineList1.append([(x1,y1),(x2,y2)])
                else:
                    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),1)
                    lineList2.append([(x1,y1),(x2,y2)])
        except:
            error=0
            #line2 = LineString([(x1,y1), (x2,y2)])
            #print line2.intersection(line2)
        #    lineList.append([(x1,y1),(x2,y2)])
          #  print theta
        points=[]
        xList=[]
    #    cv2.circle(img,(100, 100),2,(0,0,255))
        for line1L in lineList1:
            for line2L in lineList2:
                    line1 = LineString([line1L[0], line1L[1]])
                    line2 = LineString([line2L[0], line2L[1]])
                    point = line2.intersection(line1)
                    points.append(point)

                    #print point
                    try:
                        cv2.circle(img,(int(point.x), int(point.y)),3,(255,0,0))
                        xList.append(int(point.x))
                    except:
                        pass
        try:
            xAvg=int(sum(xList) / float(len(xList)))
            cv2.line(img,(xAvg, height),(xAvg, 0),(255,255,0),5)
            error = (float(xAvg) / float(width)) - 0.5
            print error
        except:
            error = 0

        if show:
             cv2.imshow("Image", img)
             cv2.waitKey(100)
            # cv2.destroyWindow("Image")
        return error



def main():
    camera = startCamera()
    frame = getFrameFromCamera(camera = camera)
    findDirectionError(frame, show = True)
    camera.close()
    cv2.destroyWindow('img')

if __name__ == '__main__':
    main()
