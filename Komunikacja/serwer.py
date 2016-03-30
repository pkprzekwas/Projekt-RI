import jsonSocket
import logging
import time

logger = logging.getLogger("RI-Project")


class PiServer(jsonSocket.ThreadedServer):
    def __init__(self):
        super(PiServer, self).__init__()
        self.timeout = 2.0

    def _processMessage(self, obj):
        """ virtual method """
        if obj != '':
            x = obj.get("x")
            y = obj.get("y")
            x, y = self._parser(x, y)
            print x, y

    @staticmethod
    def _parser(x, y):
        try:
            x = int(x)
            y = int(y)
            if x not in xrange(401):
                x, y = 0, 0
            if y not in xrange(401):
                x, y = 0, 0
        except ValueError:
            x, y = 0, 0
        return x, y

if __name__ == "__main__":
    # default port 5007
    c = PiServer()
    c.start()


# Part for testing this solution. This code need to be paced on 'Joystick' module
# (Tip: you need to import jsonSocket in your 'Joystick' module)
# Comment this if you want to create client on different machine
    time.sleep(3)
    from random import randint
    client = jsonSocket.JsonClient(address='127.0.0.1', port=5007)
    client.connect()
    for i in range(1000):
        client.sendObj({"x": randint(0, 400),
                        "y": randint(0, 400),
                        "btn_1": "TODO",
                        "btn_2": "TODO"})
        time.sleep(0.001)

    time.sleep(3)

    client.close()
    c.stop()

