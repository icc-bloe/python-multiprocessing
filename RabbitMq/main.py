__author__ = 'bloe'

import pika
from sender import Sender
from receiver import Receiver

def main():
    create_queue()
    sender = Sender()
    receiver = Receiver()
    sender.start()
    receiver.start()

def create_queue():
    connection = pika.BlockingConnection()
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    connection.close()


if __name__ == '__main__':
    main()