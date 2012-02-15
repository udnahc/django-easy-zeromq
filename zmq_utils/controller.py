import zmq

publish_socket_url = "tcp://127.0.0.1:5000"
response_socket_url = "tcp://127.0.0.1:5010"

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind(publish_socket_url)
    
context = zmq.Context()
request_socket = context.socket(zmq.REP)
request_socket.bind(response_socket_url)

while True:
    msg = request_socket.recv()
    print 'Got ', msg
    if msg == 'START':
        socket.send('START')
        socket.recv()

    if msg == 'STOP':
        socket.send('STOP')
        socket.recv()
        break

    request_socket.send("ACK")
