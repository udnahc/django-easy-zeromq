import zmq

response_socket_url = "tcp://127.0.0.1:5010"

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect(response_socket_url)


socket.send('START')
import pdb; pdb.set_trace()

    
