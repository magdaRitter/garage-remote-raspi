#!/usr/bin/env python3

from src.consumer import ConsumerThread
import logging

logging.basicConfig(filename="../log/garage-remote-raspi.log", level=logging.DEBUG, format='%(asctime)s:%(name)s:%(message)s')
logging.getLogger("pika").propagate = False


def main() -> None:
    logging.info("=== Garage remote raspi ===")

    consumers = [ConsumerThread()]
    for consumer in consumers:
        consumer.start()


if __name__ == "__main__":
    main()
