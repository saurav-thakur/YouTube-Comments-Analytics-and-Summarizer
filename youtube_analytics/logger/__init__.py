import logging
import os
import sys
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"
logs_dir_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir_path, exist_ok=True)
LOG_FILE_PATH = os.path.join(logs_dir_path, LOG_FILE)

# Create a formatter for the log entries
formatter = logging.Formatter("[ %(asctime)s ] - %(lineno)d - %(name)s - %(levelname)s - %(message)s")

# Create a file handler to write logs to the file
file_handler = logging.FileHandler(LOG_FILE_PATH)
file_handler.setFormatter(formatter)

# Create a stream handler to print logs to the console
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)

# Create the logger and add the handlers
logging.basicConfig(
    level=logging.DEBUG,
    handlers=[file_handler, stream_handler],
)