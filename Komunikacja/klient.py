import jsonSocket

class MyClient(jsonSocket.JsonClient):
    def __init__(self):
        super(MyClient, self).__init__()
        self.timeout = 2.0

if __name__ == "__main__":
    k = MyClient()
    k.connect()




