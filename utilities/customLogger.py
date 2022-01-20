import logging


class LogGen:

    @staticmethod
    def loggen():
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
            logger = logging.getLogger()
            while logger.handlers:
                logger.handlers.pop()
            filehandler = logging.FileHandler(filename=".\\Logs\\test_automation.log", mode='a')
            fileformatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
            filehandler.setFormatter(fileformatter)
            logger.addHandler(filehandler)
            logger.setLevel(logging.INFO)
            return logger
