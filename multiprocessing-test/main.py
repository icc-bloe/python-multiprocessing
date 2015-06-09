__author__ = 'bloe'

import logging
from producer import Producer
from consumer import Consumer
from multiprocessing import Queue

def start():
    logging.basicConfig(level=logging.INFO)
    logging.info("Started multiprocessing...")
    product_queue = Queue()
    task_queue = Queue()
    producer = Producer(task_queue)
    consumer = Consumer(task_queue, product_queue)
    producer.start()
    consumer.start()
    while True:
        product = product_queue.get()
        print("Received: " + str(product))

if __name__ == '__main__':
    start()
