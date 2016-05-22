
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import cv2 as cv
import numpy as np

import thread

size=(320,240)
class cameraModule:
        def __init__(self):
                self.camera = PiCamera()
                self.camera.resolution = size
                self.camera.framerate = 40
                self.rawCapture = PiRGBArray(self.camera, size=size)

                time.sleep(0.1)
                self.focusPoint=[0,0]
                self.captureFlag = False
                self.readyToCloseFlag=False


        def closeCameraModule(self):
                self.captureFlag=False


        def startCapture(self):
                self.captureFlag=True
                thread.start_new_thread(self.capture,())

        def stopCapture(self):
                self.captureFlag=False

        def line_intersection(self, line1, line2):
                xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
                ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1]) #Typo was here
                def det(a, b):
                        return a[0] * b[1] - a[1] * b[0]
                div = det(xdiff, ydiff)
                if div == 0:
                        raise Exception('lines do not intersect')

                d = (det(*line1), det(*line2))
                x = det(d, xdiff) / div
                y = det(d, ydiff) / div
                return x, y

        def capture(self):
                try:
                        for self.frame in self.camera.capture_continuous(self.rawCapture, format="bgr", use_video_port=True):
                                self.img = self.frame.array
                                img=self.img
                                img2 = img
                                A = []
                                B = []
                                C = []
                                D = []
                                img = cv.Sobel(img, -1, 1, 0)
                                img = cv.Canny(img, 100, 200, apertureSize=3)

                                linie = cv.HoughLines(img, 1, np.pi / 25, 35)
                                if linie is not None:
                                    for i in range(0, len(linie)):
                                        for rho, theta in linie[i]:
                                            a = np.cos(theta)
                                            b = np.sin(theta)
                                            x0 = a * rho
                                            y0 = b * rho
                                            x1 = int(x0 + 1000 * (-b))
                                            y1 = int(y0 + 1000 * (a))
                                            x2 = int(x0 - 1000 * (-b))
                                            y2 = int(y0 - 1000 * (a))
                                            theta = float(theta)
                                            if (theta >= 0.0 and theta <= 1.1):
                                                    A = [x1,y1]
                                                    B = [x2,y2]                                              
                                            elif (theta >2.6 and theta < 3.1):
                                                    C = [x1,y1]
                                                    D = [x2,y2]
                                            if A != [] and B!=[] and C != [] and D != [] :
                                                    center = self.line_intersection([A, B], [C, D])
                                                    if 150 <= center[0] <= 170 :                                                            
                                                            cv.line(img2, (A[0], A[1]), (B[0], B[1]), (0, 0, 255), 2)
                                                            cv.line(img2, (C[0], C[1]), (D[0], D[1]), (0, 0, 255), 2)
                                                            cv.circle(img2, center , 5 , (255,0,0), thickness = -1)

                                                
                                cv.imshow('obraz', img2)

                                #cv2.imshow('img',self.img)
                                key = cv2.waitKey(10) & 0xFF
                                self.rawCapture.truncate(0)
                                if self.captureFlag==False:
                                        break
                finally:
                        self.camera.close()
                        cv2.destroyWindow('img')
                        self.readyToCloseFlag=True

def main():
    c=cameraModule()
    c.startCapture()
    try:
        while True:
            pass
    finally:
        c.stopCapture()

if __name__ == '__main__':
    main()
