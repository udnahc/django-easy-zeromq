import zmq
from zmq_utils.utils import Worker

class Ventilator(Worker):
    def ventilate(self):
        print "Is it even comming here "
        self.logger.info("Ventilator: Sending message to a logger ")
        self.send_message_to_worker('Some Message', 'trashbin')
        self.logger.info("Ventilator: Message to logger sent")       

    def collect(self, work_message):
        print "Ventilator: This should never execute in an ideal world "

    def stop_worker(self):
        print "Ventilator: Do something to stop the ventilator"

if __name__ == '__main__':
    controller_is_listening_at = "tcp://127.0.0.1:5010"
    controller_is_publishing_to = "tcp://127.0.0.1:5000"
    
    trashbins_url = "tcp://127.0.0.1:6000"

    ventilator = Ventilator(controller_is_publishing_to, controller_is_listening_at, None, trashbins_url , zmq.PUSH)
    print 'Runnning this ventilator '
    ventilator.listen()
