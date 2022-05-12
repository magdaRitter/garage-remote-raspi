from rabbitmq import Config
from cipher import Encryptor
from process import Process

import pika
import logging
import traceback
from time import sleep

logger = logging.getLogger(__name__)


class Consumer:
    def __init__(self):
        pass

    def start(self) -> bool:
        if not self.__make_connection():
            logger.error("Could not make consumer connection")
            return False

        return True

    @staticmethod
    def __on_message(channel, method, properties, body) -> bool:
        try:
            message = Encryptor().decrypt(body)
            print(message)
            if not message:
                logger.error("Could not decrypt the message!")
                return False

            logger.info("Consumer received '{}'".format(message))

            process = Process()
            return process.process(message)
        except Exception as e:
            traceback.print_exc()
            logger.debug("An exception was thrown while handling incoming message")

    def __make_connection(self) -> bool:
        result = False
        while True:
            try:
                connection = pika.BlockingConnection(
                    pika.ConnectionParameters(host=Config.host))

                channel = connection.channel()
                channel.queue_bind(queue=Config.queue,
                                   exchange=Config.topic_exchange_name,
                                   routing_key=Config.routing_key)
                channel.basic_consume(Config.queue, self.__on_message,
                                      auto_ack=True)

                logger.info("Consumer is listening...")
                channel.start_consuming()

                result = True
            except pika.exceptions.ChannelClosedByBroker:
                logger.debug("Channel was closed by broker, retrying...")
                sleep(5)
                continue
            except pika.exceptions.ConnectionClosedByBroker:
                logger.debug("Connection was closed by broker, retrying...")
                sleep(5)
                continue
            except pika.exceptions.AMQPConnectionError:
                logger.debug("AMQP Connection error occured, retrying...")
                sleep(10)
                continue
            except Exception as e:
                traceback.print_exc()
                logger.debug("An exception was thrown while making the consumer connection")

        return result
