import socket
import time
from threading import Thread
import a_star


class Com:

    def receiver(self):
        TCP_IP = '10.0.0.5'
        TCP_PORT = 50100

        BUFFER_SIZE = 1024
        s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s2.bind((TCP_IP, TCP_PORT))
        s2.listen(1)
        conn, addr = s2.accept()
        print 'Connection address:', addr
        while 1:
            data = conn.recv(BUFFER_SIZE)
            if not data: break
            print(data)
            self.ride(data)

        conn.close()

    def ride(self, message):
        if message == '8':
            self.robot.motors(350, 350)
        if message == '2':
            self.robot.motors(-350, -350)
        if message == '6':
            self.robot.motors(350, -350)
        if message == '4':
            self.robot.motors(-350, 350)
        if message == '0':
            self.robot.motors(0, 0)
        if message == '5':
            self.robot.play_notes("o4l16ceg>c8")


    def __init__(self):
        self.robot = a_star.AStar()
        try:
            self.t1 = Thread(target=self.receiver, args=())
            self.t1.start()

        except:
            print "Error: unable to start thread"

        self.message = None


if __name__ == "__main__":
    com = Com()

    while True:
        time.sleep(0.5)
