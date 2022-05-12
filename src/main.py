from consumer import ConsumerThread
import logging
import sys

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(name)s:%(message)s',
                    handlers=[
                        # logging.FileHandler("../log/debug.log"),
                        logging.StreamHandler(sys.stdout)
                    ]
                    )
logging.getLogger("pika").propagate = False


def main() -> None:
    logging.info("=== Garage remote raspi ===")

    consumers = [ConsumerThread()]
    for consumer in consumers:
        consumer.start()


if __name__ == "__main__":
    main()
