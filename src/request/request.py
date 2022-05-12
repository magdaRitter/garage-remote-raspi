import traceback
from rabbitmq import Config
from signal import SignalTrigger
from publisher import Publisher
import logging

logger = logging.getLogger(__name__)


class Request:
    def __init__(self, signal_type, signal_id):
        self.__signal_type = signal_type
        self.__signal_id = signal_id

    def process(self) -> None:
        response = self.__send_signal()

        if not self.__respond(response):
            logger.error("Could not send response to the request with id {}".format(self.__signal_id))

    def __respond(self, response) -> bool:
        publisher = Publisher()
        return publisher.send(response)

    def __send_signal(self) -> str:
        status = False

        try:
            status = SignalTrigger().trigger(self.__signal_type)
        except Exception as e:
            logger.debug("An exception was thrown while triggering a signal with id {}".format(self.__signal_id))
            traceback.print_exc()

        response = "{}_{}_{}_{}".format(Config.RESPONSE_KEY, self.__signal_type.to_str(), self.__signal_id, status)

        return response
