from multiprocessing import Process
import logging

class Consumer(Process):

    def run(self):
        print("Started consumer")
        while self.running:
            packet = self.taskQueue.get()
            product = packet.content * packet.content
            self.productQueue.put(product)

    def __init__(self,taskQueue, productQueue):
        super(Consumer, self).__init__()
        logging.info("Starting consumer process")
        self.running = True
        self.taskQueue = taskQueue
        self.productQueue = productQueue
