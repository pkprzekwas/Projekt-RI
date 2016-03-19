import socket
from threading import Thread


class TCPCommunication(object):
    """
    Class for handling TCP-IP communication between two clients.
    Creates two sockets: one for sending, and one for receiving data.
    Sockets are managed in two threads running alternately.
    Data is validate and parse before sending.
    """
    def __init__(self, receiver=0, sender=0, ip_addr='localhost'):
        # TODO change to PC ip_addr
        self.tcp_ip = 'localhost'
        self.tcp_sender_port = int(sender)
        self.tcp_receiver_port = int(receiver)
        self.ip_addr = ip_addr
        self.buffer_size = 1024

    def start_threads(self):
        try:
            t1 = Thread(target=self._sender, args=())
            t2 = Thread(target=self._receiver, args=())
            t1.start()
            t2.start()
            while True:
                pass
        # TODO specify exception type
        except Exception:
            print("Error: unable to start thread")

    def _sender(self):
        _ = raw_input("Press enter after connecting...")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip_addr, self.tcp_sender_port))

        # setting connection
        s.send('?')
        data = s.recv(self.buffer_size)

        while True:
            # TODO add const heartbeat interval
            if data:
                ack = "ack"
                # TODO validation
                if data:
                    s.send(ack)
                else:
                    s.send("Invalid command")
            else:
                break
        s.close()

    def _receiver(self):
        """
        Creates interface for receiving data.
        Handles loop for receiving data.
        :return:
        """
        self.tcp_ip = 'localhost'
        s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s2.bind((self.tcp_ip, self.tcp_receiver_port))
        s2.listen(1)
        conn, addr = s2.accept()

        while True:
            data = conn.recv(self.buffer_size)
            if not data:
                break
            else:
                # TODO validate and send command do engine
                print(data)
                # resend ack of proper command
                conn.send('ack')
        conn.close()


# if __name__ == "__main__":
#     # TODO add ip_addr here for PC addr
#     receiver_port = raw_input('Receiver port: ')
#     sender_port = raw_input('Sender port: ')
#     ip_addr = raw_input('Sender port: ')
#     connection = TCPCommunication(receiver_port, sender_port, ip_addr)
#     connection.start_threads()