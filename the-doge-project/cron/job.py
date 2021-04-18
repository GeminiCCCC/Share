import datetime
import logging
import json


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s [%(filename)s:%(lineno)d %(levelname)s] %(message)s',
                    datefmt="%Y-%m-%d %H:%M:%S")

VERSION = "0.1.0"


def main():
    data = {"timestamp": datetime.datetime.now().isoformat()[0:19], "version": VERSION}
    logging.info(json.dumps(data))


if __name__ == "__main__":
    main()
