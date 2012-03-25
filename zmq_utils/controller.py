import zmq

publish_socket_url = "tcp://127.0.0.1:5000"
response_socket_url = "tcp://127.0.0.1:5010"
logger_socket_url = "tcp://127.0.0.1:2000"

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind(publish_socket_url)
    
context = zmq.Context()
request_socket = context.socket(zmq.REP)
request_socket.bind(response_socket_url)

while True:
    msg = request_socket.recv()
    print 'Controller: Got message ', msg
    if msg == 'START':
        print 'Controller: Starting something, this is just a stub '
        socket.send('START')
        request_socket.send("ACK")

    if msg == 'START_PROCESS':
        print 'Starting the process '
        socket.send('START_PROCESS')
        request_socket.send("ACK")

    if msg == 'STOP_PROCESS':
        print 'Starting the process '
        socket.send('STOP_PROCESS')
        request_socket.send("ACK")

    if msg == 'STOP':
        print 'Controller: Stopping something, this is a stub again '
        socket.send('STOP')
#        socket.recv()
        request_socket.send("ACK")
        context.destroy()
        break

