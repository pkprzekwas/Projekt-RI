from SocketServer import BaseRequestHandler, TCPServer


class EchoHandler(BaseRequestHandler):
    ACK = 'ack'

    def handle(self):
        print('Got connection from', self.client_address)
        while True:
            # expected command two integers separated vie comma (e.g. 100, 200)
            command = self.request.recv(8192)
            x, y = parser(command)
            print x, y # testing
            # sending order to engines here
            if not command:
                # if connection lost engines stop here
                break
            self.request.send(self.ACK)


def parser(command):
    try:
        vals = command.split(',')
        x, y = int(vals[0]), int(vals[1])
        if x not in xrange(401):
            x, y = 0, 0
        if y not in xrange(401):
            x, y = 0, 0
    except ValueError:
        x, y = 0, 0
    return x, y


if __name__ == '__main__':
    serv = TCPServer(('', 20002), EchoHandler)
    serv.serve_forever()