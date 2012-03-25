import logging
import zmq
from zmq_utils.utils import Worker

logger_socket_url = "tcp://127.0.0.1:2000"

context = zmq.Context().instance()
subscriber_socket = context.socket(zmq.SUB)
subscriber_socket.connect(logger_socket_url)
subscriber_socket.setsockopt(zmq.SUBSCRIBE,"")

while True:
    log_message = subscriber_socket.recv_multipart()
    print log_message
