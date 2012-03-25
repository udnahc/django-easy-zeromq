import zmq
import logging

class Worker(object):
    def __init__(self, controller_sub_url, controller_rep_url, bind_to, connect_to, socket_type):
        self.context = zmq.Context().instance()
        self.bind_to = bind_to
        self.controller_sub_url = controller_sub_url
        self.controller_rep_url = controller_rep_url
        self.socket_type = socket_type
        self.connect_to = connect_to
        self.create_self()
        self.subscribe_to_controller()
        self.connect_to_controller()
        self.create_logger()

    def create_logger(self):
        from zmq.log.handlers import PUBHandler
        logger_publisher = self.context.socket(zmq.PUB)
        logger_publisher.bind("tcp://127.0.0.1:2000")
        handler = PUBHandler(logger_publisher)
        self.logger = logging.getLogger()
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)
        
    def create_self(self):
        self.worker = self.context.socket(self.socket_type)
        if self.bind_to:
            self.worker.bind(self.bind_to)

    def subscribe_to_controller(self):
        self.subscriber_socket = self.context.socket(zmq.SUB)
        self.subscriber_socket.connect(self.controller_sub_url)
        self.subscriber_socket.setsockopt(zmq.SUBSCRIBE, "")

    def connect_to_controller(self):
        self.command_request_socket = self.context.socket(zmq.PUSH)
        self.command_request_socket.connect(self.controller_rep_url)

    def send_message_to_controller(self, message):
        self.command_request_socket.send(message)

    def unbind_all(self):
        self.context.destroy()

    def stop(self):
        self.listening = False
        self.unbind_all()
        
    def send_message_to_worker(self, work_message, worker_key):
        if worker_key=='trashbin':
            self.worker.connect("tcp://127.0.0.1:6000")
            self.worker.send(work_message)

    def listen(self):
        poller = zmq.Poller()
        poller.register(self.subscriber_socket, zmq.POLLIN)

        if self.bind_to:
            print "Worker: This is a trashbin "
            poller.register(self.worker, zmq.POLLIN)
  
        while True:
            socks = dict(poller.poll())
            
            if socks.get(self.subscriber_socket) == zmq.POLLIN:
                controller_message = self.subscriber_socket.recv()
                print "Worker: Received a controller message ", controller_message
                if controller_message == 'START_PROCESS':
                    self.ventilate()
                
                if controller_message == 'STOP_PROCESS':
                    self.stop_worker()
                
            if self.bind_to:
                if socks.get(self.worker) == zmq.POLLIN:
                    work_message = self.worker.recv()
                    print  "Worker: Received from fellow worker ", work_message
                    self.collect(work_message)

def create_publisher_socket(port_no):
    # Create PUB socket on this port_no
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind(port_no)

def create_subscriber_socket(port_no):
    # Create subscriber socket on this port_no
    pass

def create_push_socket(port_no):
    # Create push socket on this port_no
    pass

def create_pull_socket(port_no):
    # Create pull socket on this port_no
    pass


def create_request_socket(port_no):
    # Create request socket on this port_no
    pass

def create_response_socket(port_no):
    # Create response socket on this port_no
    pass

