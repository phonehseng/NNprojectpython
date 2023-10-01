import os
from datetime import datetime
import logging

time_tested = datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
file_location = os.path.relpath(__file__)
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
log_path = os.path.join(ROOT_DIR, 'Logs')
if not os.path.exists(log_path):
    os.mkdir(log_path)
log_file = os.path.join(log_path, f"{time_tested}_logfile.log")
#set up logger
logger = logging.getLogger(log_file)
logger.setLevel(logging.DEBUG)
#formatting the log output
formatter = logging.Formatter(
    "%(asctime)s -- %(message)s"
)
#Setting up file handler, this will write the log to the log file
file_handler = logging.FileHandler(log_file)
file_handler.setFormatter(formatter)
#Setting up Stream handler, this will print the log in the terminal
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.debug("This is DEBUG level logs.")
logger.info("This is INFO level logs.")
logger.warning("This is WARNING level logs")
logger.error("This is ERROR level logs")
logger.critical("This is CRITICAL level logs")
