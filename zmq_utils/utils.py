import zmq

class Worker(object):
    def __init__(self, controller_sub_url, controller_rep_url, worker_listen_url, bind_to, socket_type):
        self.context = zmq.Context().instance()
        self.bind_to = self.bind_to
        self.controller_sub_url = controller_sub_url
        self.controller_rep_url = controller_rep_url
        self.worker_listen_url = Worker_listen_url
        self.listener = False

    def subscribe_to_controller(self):
        self.subscriber_socket = self.context.socket(zmq.SUB)
        self.subscriber_socket.connect(controller_sub_url)
        self.subscriber_socket.setsockopt(zmq.SUBSCRIBE, "")
    
    def bind_to_other_workers(self):
        self.other_worker_socket = self.context.socket(socket_type)
#        self.worker_listen = self.other_worker_socket.

    def send_message_to_controller(self, message):
        self.command_request_socket = self.context.socket(zmq.PUSH)
        self.command_request_socket.connect(self.controller_rep_url)

    def listen_to_other_workers(self):
        poller = zmq.Poller()
        poller.register(self.subscriber_socket, zmq.POLLIN)

        if self.worker_listen_url:
            poller.register(self.Worker_listen_url, zmq.POLLIN)

        
        while True:
            pass

    def bind_all(self):
        self.subscribe_to_controller()
        self.subscribe_to_other_workers()

    def unbind_all(self):
        self.context.destroy()

    def stop(self):
        self.listening = False
        self.unbind_all()

    def listen(self):
        pass

    def start(self):
        pass

    


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
