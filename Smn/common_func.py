import logging
import sys


def get_logger(logger_name):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(threadName)s - %(name)s - %(funcName)s - %(lineno)d - %(message)s",
        handlers=[logging.StreamHandler(sys.stdout), ]
    )
    logger = logging.getLogger(logger_name)
    return logger

