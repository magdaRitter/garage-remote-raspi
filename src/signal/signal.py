import logging

logger = logging.getLogger(__name__)


class Signal:
    def __init__(self, type):
        self.__type = type

    def trigger(self) -> bool:
        logger.debug("Signal for {} is being fired".format(self.__type))
        result = False

        return result
