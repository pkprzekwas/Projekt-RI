
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import cv2 as cv
import numpy as np

import thread

#size=(1280,720)
#size=(640,480)
#size=(320,240)
size = (160,120)
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


def main():
    camera = startCamera()
    try:
        while True:
            frame = getFrameFromCamera(camera = camera)
            cv2.imshow("Image", frame)
            cv2.waitKey(100)
    finally:
        camera.close()
        cv2.destroyWindow('img')

if __name__ == '__main__':
    main()
