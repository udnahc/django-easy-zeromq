import zmq

# Subscribe to Subscriber for commands from controller
context = zmq.Context()
subscriber_socket = context.socket(zmq.SUB)
subscriber_socket.connect("tcp://127.0.0.1:5000")
subscriber_socket.setsockopt(zmq.SUBSCRIBE, "")


# This is a trashbin so it will accept something from the ventilator
pull_socket = context.socket(zmq.PULL)
pull_socket.bind("tcp://127.0.0.1:6000")

poller = zmq.Poller()
poller.register(subscriber_socket, zmq.POLLIN)
poller.register(pull_socket, zmq.POLLIN)
    
while True:
    socks = dict(poller.poll())
    if socks.get(subscriber_socket) == zmq.POLLIN:
        subscriber_message = subscriber_socket.recv()
        print 'Subscriber Message:', subscriber_message
        if subscriber_message == 'STOP':
            break

    if socks.get(pull_socket) == zmq.POLLIN:
        pull_socket_message = pull_socket.recv()
        print 'Pull Socket Message:', pull_socket_message
