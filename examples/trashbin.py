import zmq
from zmq_utils.utils import Worker

class Trashbin(Worker):
    def ventilate(self):
        print "Trashbin: This is a Trashbin so no ventilation "
    
    def collect(self, work_message):
        print "Trashbin: Received something from Ventilator ", work_message
    
    def stop_worker(self):
        print "Trashbin: Have to do something to stop this worker "

if __name__ == '__main__':
    controller_is_listening_at = "tcp://127.0.0.1:5010"
    controller_is_publishing_to = "tcp://127.0.0.1:5000"
    
    bind_to  = "tcp://127.0.0.1:6000"

    trashbin = Trashbin(controller_is_publishing_to, controller_is_listening_at, bind_to, [], zmq.PULL)
    print 'Runnning this trashbin '
    trashbin.listen()
