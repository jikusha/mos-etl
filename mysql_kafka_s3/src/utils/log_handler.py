import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)
logger.propagate = False
streamHandler = logging.StreamHandler(sys.stdout)
logger.addHandler(streamHandler)
streamHandler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(funcName)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))
logger.setLevel(logging.INFO)

logger.info("Logger is created successfully!!!")