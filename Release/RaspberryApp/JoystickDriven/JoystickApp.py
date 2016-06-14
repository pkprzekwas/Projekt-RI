import jsonSocket
import logging
import time
import a_star
#import speech

logger = logging.getLogger("RI-Project")
robot = a_star.AStar()

class PiServer(jsonSocket.ThreadedServer):
    def __init__(self):
        super(PiServer, self).__init__(address='192.168.0.11')
        self.timeout = 2.0
    #    self.voice=speech.Speech()


    def _processMessage(self, obj):
        """ virtual method """
        if obj != '':
            x = obj.get("x")
            y = obj.get("y")
            obstacle = obj.get("obstacle")
            x, y = self._parser(x, y)
            if obstacle=="1":
                pass
            #    self.voice.obstacle()
            #print x, y, obstacle
	    try:
	   	    print robot.read_distance()[0]
	    except:
	        pass

    @staticmethod
    def _parser(x, y):
        try:
            x = int(x*0.65)
            y = int(y*0.65)
	    robot.motors(y, x)
        except ValueError:
            x, y = 0, 0
        return x, y

if __name__ == "__main__":
    # default port 5007
    c = PiServer()
    c.start()
