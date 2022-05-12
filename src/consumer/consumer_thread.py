from consumer import Consumer

import threading
import logging

logger = logging.getLogger(__name__)


class ConsumerThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        self.__consumer = Consumer()
        super(ConsumerThread, self).__init__(*args, **kwargs)

    def run(self) -> None:
        logger.debug("ConsumerThread is starting")
        if not self.__consumer.start():
            logger.error("Failed to start consumer thread")
