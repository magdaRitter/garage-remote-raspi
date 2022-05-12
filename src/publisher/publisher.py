from rabbitmq import Config
from cipher import Encryptor
import pika
import logging

logger = logging.getLogger(__name__)


class Publisher:
    def __init__(self):
        self.__channel = None
        self.__connection = None

    def __make_connection(self) -> bool:
        result = False
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(Config.host))
            channel = connection.channel()
            channel.queue_declare(queue=Config.queue)

            self.__channel = channel
            self.__connection = connection

            result = True
        except Exception as e:
            logger.debug("An exception was thrown while making connection for publisher")
            logger.debug(e)

        logger.debug("Publisher is ready")
        return result

    def send(self, message) -> bool:
        result = False
        if not self.__make_connection():
            logger.error("Publisher could not establish connection")
            return result

        try:
            body = Encryptor().encrypt(message)
            if not body:
                logger.error("Could not encrypt the message!")
                return False

            self.__channel.basic_publish(Config.topic_exchange_name, Config.routing_key, body=body)
            logger.info("Published message: " + message)

            self.__connection.close()
            result = True
        except Exception as e:
            logger.debug("An exception was thrown while publishing a message")
            logger.debug(e)

        return result
