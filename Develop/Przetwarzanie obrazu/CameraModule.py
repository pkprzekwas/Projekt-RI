
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
                                A = []
                                B = []
                                C = []
                                D = []
                                height, width, _ = img.shape
                                img = img[height*0.55:height, 20:width-20]
                                img2 = img
                                img = cv.Sobel(img, -1, 1, 0)
                                img = cv.Canny(img, 60, 120, apertureSize=3)
                                punkty = []
                                linie = cv.HoughLines(img, 1, np.pi / 20, 50)
                                if linie is not None:
                                        for i in range(0, len(linie)):
                                                for rho, theta in linie[i]:
                                                        a = np.cos(theta)
                                                        b = np.sin(theta)
                                                        x0 = a * rho
                                                        y0 = b * rho
                                                        x1 = int(x0 + 1000 * (-b))
                                                        y1 = int(y0 + 1000 * a)
                                                        x2 = int(x0 - 1000 * (-b))
                                                        y2 = int(y0 - 1000 * a)
                                                        theta = float(theta)
                                                        if 0.0 <= theta < 1.3:
                                                                A = (x1, y1)
                                                                B = (x2, y2)
                                                                punkty.append([A, B])
                                                        elif 2.0 < theta < 3.14:
                                                                C = (x1, y1)
                                                                D = (x2, y2)
                                                                punkty.append([C, D])

                                suma = 0
                                n = 0

                                for x in xrange(0, punkty.__len__()):
                                        cv.line(img2, punkty[x][0], punkty[x][1], (0, 0, 255), 2)
                                        for y in xrange(x, punkty.__len__()):
                                                center = self.line_intersection(punkty[x], punkty[y])
                                                if center:
                                                        if 0 <= center[0] <= width:
                                                                suma += center[0]
                                                                n += 1
                                                                cv.circle(img2, center, 5, (255, 0, 0), thickness=-1)

                                h, w, _ = img2.shape
                                if n != 0:
                                        avg = suma/n
                                        cv.rectangle(img2, (avg-5, h/2-5), (avg+5, h/2+5), color=(0, 255, 0), thickness=2)

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
