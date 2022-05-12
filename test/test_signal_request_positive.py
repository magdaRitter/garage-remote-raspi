from consumer import ConsumerThread
from publisher import Publisher

import time


class TestSignalRequestPositive:

    def setup_class(cls):
        consumer_thread = ConsumerThread()
        consumer_thread.daemon = True
        consumer_thread.start()

        cls.test_msg_garage = "GARAGE_5c733319-c3b9-4e74-be95-540f87c7468d"

    def test_signal_request_positive(self):
        publisher = Publisher()
        assert publisher.send(self.test_msg_garage)

        time.sleep(1)
