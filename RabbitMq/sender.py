__author__ = 'bloe'

import pika
from multiprocessing import Process

class Sender(Process):
    def __init__(self):
        super().__init__()
        self.connection = None

    def create_connection(self):
        self.connection = pika.BlockingConnection()

    def run(self):
        self.create_connection()
        channel = self.connection.channel()
        while True:
            channel.basic_publish(exchange='',
                                  routing_key='hello',
                                  body='Hello World!')

