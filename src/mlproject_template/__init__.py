import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s : %(module)s: %(message)s]"
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_log.log")
os.makedirs(log_dir, exist_ok=True)

# Setting up the logger
logger = logging.getLogger("mlProjectLogger")
logger.setLevel(logging.INFO)

# File handler to log to a file
file_handler = logging.FileHandler(log_filepath)
file_handler.setFormatter(logging.Formatter(logging_str))

# Stream handler to log to console
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(logging.Formatter(logging_str))

# Adding handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
