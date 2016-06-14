import serial
import time
import re


class Nunchuck(object):
    def __init__(self):
        try:
            self.serial = serial.Serial('COM9', 19200, timeout=0.1)
            self.vect = []
        except:
            pass

    def getData(self):
        try:
            line = str(self.serial.readline())
            line = re.sub("[^0-9^.]", " ", line)
            self.vect = line.split(' ')
            self.vect = list(filter(None, self.vect))
        except:
            print('Data could not be read')


if __name__ == "__main__":
    nun = Nunchuck()
    while True:
        nun.getData()
        try:
            x = (float(nun.vect[0]) - 123) / 123
            y = (float(nun.vect[1]) - 129) / 123
            print (nun.vect)
        except:
            pass
