import pyttsx
import time
from random import randint


class Speech:
    def createDicts(self):
        self.obstacleList = [
            "sorry",
            "I want to drive this way",
            "Dear Human, you are on my path"]
        print(self.obstacleList)

    def __init__(self):
        self.engine = pyttsx.init()
        self.createDicts
        self.engine.setProperty('rate', 160)
        self.engine.say('Initializing')
        self.engine.runAndWait()

    def say(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def obstacle(self):
        self.say(self.obstacleDict[randint(0, len(self.obstacleList))])


def main():
    s = Speech()
    time.sleep(2)
    s.obstacle()
    time.sleep(2)


if __name__ == '__main__':
    main()
