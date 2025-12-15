import logging
import os

LOG_DIR = 'log'
LOG_FILE = os.path.join(LOG_DIR,'app.log')

os.makedirs(LOG_DIR,exist_ok=True)

logging.basicConfig(level=logging.INFO,format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
                    handlers=[
                        logging.FileHandler(LOG_FILE),
                        logging.StreamHandler()
                    ]
                    )

def get_logger(name):
    return logging.getLogger(name)