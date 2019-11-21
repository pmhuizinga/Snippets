# sample script for process logging using the logging library

import logging

# setup
logger = logging.getLogger(__name__)  # initialize logger
logger.handlers = []
c_handler = logging.StreamHandler()  # Create handlers
c_format = logging.Formatter('%(levelname)s - %(message)s')
c_handler.setFormatter(c_format)  # Create formatters and add it to handlers
logger.addHandler(c_handler)  # Add handlers to the logger
logger.setLevel(logging.DEBUG)

# actual logging
logger.debug(f'fill log text here')
