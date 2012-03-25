import zmq

logger_socket_url = "tcp://127.0.0.1:2000"

class Client(object):

    def __init__(self):
        self.controller_is_listening_at = "tcp://127.0.0.1:5010"
        self.controller_is_publishing_to =  "tcp://127.0.0.1:5000"

    def send_start_signal(self):
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect(self.controller_is_listening_at)
        socket.send('START')
        ack = socket.recv()
        print "Client: Acknowledgement received after stop ",ack

    def send_stop_signal(self):
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect(self.controller_is_listening_at)
        socket.send('STOP')
        ack = socket.recv()
        print "Client: Acknowledgement received after stop ",ack
    

    def send_start_process_signal(self):
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect(self.controller_is_listening_at)
        socket.send('START_PROCESS')
        ack = socket.recv()
        print "Client: Acknowledgement received after start process ",ack

    def send_stop_process_signal(self):
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect(self.controller_is_listening_at)
        socket.send('STOP_PROCESS')
        ack = socket.recv()
        print "Client: Acknowledgement received after stop process ",ack

    
