from src.rabbitmq import Config
from src.request import RequestThread
from src.util import message_parser
from src.signal import SignalType
import logging

logger = logging.getLogger(__name__)


class Process:
    def __init__(self):
        self.__response_key = Config.RESPONSE_KEY

    def process(self, request_message) -> None:
        if not self.__should_process(request_message):
            logger.debug("No request to process found")
            return

        self.__start_request(request_message)

    def __should_process(self, request_message) -> bool:
        result = False

        if self.__response_key not in request_message:
            logger.debug("There is a request to start")
            result = True

        return result

    def __start_request(self, request_message):
        request_type = SignalType.from_str(message_parser.extract_request_type(request_message))
        request_id = message_parser.extract_request_id(request_message)

        request_thread = RequestThread(request_type, request_id)
        request_thread.start()
