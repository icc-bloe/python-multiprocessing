__author__ = 'bloe'

import pika
from multiprocessing import Process

class Receiver(Process):
    def __init__(self):
        super().__init__()
        self.connection = None

    def create_connection(self):
        self.connection = pika.BlockingConnection()

    def message_received(self, ch, method, properties, body):
        print(" [x] Received " + body.decode("utf-8"))

    def run(self):
        self.create_connection()
        channel = self.connection.channel()
        channel.basic_consume(self.message_received,
                      queue='hello',
                      no_ack=True)

        channel.start_consuming()
