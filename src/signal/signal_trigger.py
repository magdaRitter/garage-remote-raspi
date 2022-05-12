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

        if SignalType.BOTH == type:
            result = (self._fire_garage_signal() and self._fire_gate_signal())
        if SignalType.GARAGE == type:
            result = self._fire_garage_signal()
        if SignalType.GATE == type:
            result = self._fire_gate_signal()

        return result

    def _fire_garage_signal(self) -> bool:
        return self.__fire_signal(16)
    
    def _fire_gate_signal(self) -> bool:
        return self.__fire_signal(20)

    def __fire_signal(self, led_signal) -> bool:
        result = False

        try:
            remotePin = LED(led_signal)
            remotePin.on()
            sleep(1)
            remotePin.off()

            result = True
        except Exception as e:
            logger.error("Could not send signal: {}".format(traceback.format_exception_only()))
            traceback.print_exc()

        return result