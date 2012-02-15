from zmq_utils.utils import Worker
import zmq



class Ventilator(Worker):
# Subscribe to Subscriber for commands from controller

# This is a ventilator so this will Push something to the trashbin
request_socket = context.socket(zmq.PUSH)
request_socket.connect("tcp://127.0.0.1:6000")

while True:
    subscriber_message = subscriber_socket.recv()
    
    if subscriber_message:
        print "Command from the control center . . . " , subscriber_message

    if subscriber_message == 'START':
        import random
        for i in range(100):
            random_number = random.randrange(1,10)
            request_socket.send(str(random_number))

    if subscriber_message == 'STOP':
        break


if __name__ == '__main__':
    
    print 'Run this ventilator '
