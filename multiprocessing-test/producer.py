from multiprocessing import Process
import random
import logging
from packet import Packet

class Producer(Process):

    def run(self):
        print("Started producer")
        while True:
            packet = Packet(random.randint(0, 100))
            self.taskQueue.put(packet)

    def __init__(self, taskQueue):
        super(Producer, self).__init__();
        logging.info("Starting producer process")
        self.running = True
        self.taskQueue = taskQueue
