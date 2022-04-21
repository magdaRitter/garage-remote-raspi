from src.request import Request

import threading
import logging

logger = logging.getLogger(__name__)


class RequestThread(threading.Thread):
    def __init__(self, request_type, request_id, *args, **kwargs):
        super(RequestThread, self).__init__(*args, **kwargs)

        self.__request_type = request_type
        self.__request_id = request_id

    def run(self) -> None:
        logger.debug("Starting the request thread (type = {}, id = {})".format(self.__request_type, self.__request_id))
        request = Request(self.__request_type, self.__request_id)
        request.process()
