from src.rabbitmq import Config
from src.util import parse_utf_8
from src.process import Process

import pika
import logging

logger = logging.getLogger(__name__)


class Consumer:
    def __init__(self):
        self.__channel = None

    def start(self) -> bool:
        if not self.__make_connection():
            logger.error("Could not make consumer connection")
            return False
        if not self.__start_consuming():
            logger.error("Could not start consumer")
            return False

        return True

    @staticmethod
    def __callback(channel, method, properties, body) -> None:
        message = parse_utf_8(body)
        logger.info("Consumer received '{}'".format(message))

        process = Process()
        process.process(message)

    def __make_connection(self) -> bool:
        result = False
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=Config.host))

            channel = connection.channel()
            channel.queue_bind(queue=Config.queue,
                               exchange=Config.topic_exchange_name,
                               routing_key=Config.routing_key)
            channel.basic_consume(Config.queue, self.__callback,
                                  auto_ack=True)

            self.__channel = channel

            result = True
        except Exception as e:
            logger.debug("An exception was thrown while making the consumer connection")
            logger.debug(e)

        return result

    def __start_consuming(self) -> bool:
        result = False
        try:
            logger.info("Consumer is listening...")
            self.__channel.start_consuming()

            result = True
        except Exception as e:
            logger.debug("An exception was thrown while starting the consumer")
            logger.debug(e)

        return result
