import logging
from Config.config import TestData


class LogGen:
    @staticmethod
    def loggen():
        print("creating logger")
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        logging.basicConfig(filename=TestData.LOG_FILE_PATH,
                            format="%(asctime)s: %(levelname)s: %(message)s",
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        print("creating created")
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        print(logger.handlers)
        return logger