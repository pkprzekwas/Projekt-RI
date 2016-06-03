__author__ = 'Jakub'
import nunchuck
import controller
from math import sqrt
import time
import jsonSocket

def main():
    pad = nunchuck.Nunchuck()
    client = jsonSocket.JsonClient(address='10.0.0.4', port=5007)
    client.connect()
    prevButton1="0"
    obstacle="0"
    while True:
        pad.getData()
        try:
            y = (float(pad.vect[0]) - 123) / 123
            x = -(float(pad.vect[1]) - 129) / 123
        except:
            continue
        speed = sqrt(y ** 2 + x ** 2)
        angle = controller.angle(x, y, speed)
        scaled = controller.scale(angle, speed)


        if prevButton1=="0" and pad.vect[5]=="1":
            obstacle="1"
            prevButton1="1"
        else:
            obstacle="0"

        if pad.vect[5]=="0":
            prevButton1="0"

        print(scaled)
        client.sendObj({"x": int(scaled[0]),
                        "y": int(scaled[1]),
                        "obstacle": obstacle,
                        "btn_2": "TODO"})
        #controller.send(*scaled)



if __name__ == '__main__':
    main()
    # time.sleep(3)
    # from random import randint
    # client = jsonSocket.JsonClient(address='192.168.0.15', port=5007)
    # client.connect()
    # for i in range(1000):
    #     client.sendObj({"x": randint(0, 400),
    #                     "y": randint(0, 400),
    #                     "btn_1": "TODO",
    #                     "btn_2": "TODO"})
    #     time.sleep(0.001)
