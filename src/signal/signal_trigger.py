from gpiozero import LED
from time import sleep
from .signal_type import SignalType
import logging
import traceback

logger = logging.getLogger(__name__)


class SignalTrigger:
    def __init__(self):
        pass

    def trigger(self, type) -> bool:
        logger.debug("Signal for {} is being fired".format(type))
        result = False

        try:
            led_signal = 16 if SignalType.GARAGE == type else 20
            remotePin = LED(led_signal)
            remotePin.on()
            sleep(1)
            remotePin.off()

            result = True
        except Exception as e:
            logger.error("Could not send signal: {}".format(traceback.format_exception_only()))
            traceback.print_exc()

        return result
