import os
import logging
from datetime import datetime

# make a log dir.
LOG_DIR= 'logs'
LOG_DIR_PATH= os.path.join(os.getcwd(), LOG_DIR)

# Create a log directory.
os.makedirs(LOG_DIR, exist_ok= True)

# Create a file with timestamp as name.
CURR_TIME_STAMP= f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
file_name= f"log_at_{CURR_TIME_STAMP}"
log_filepath= os.path.join(LOG_DIR, file_name)

# Inititate.
logging.basicConfig(level= logging.INFO,
                    filename= log_filepath,
                    format= "%(asctime)s %(levelname)s %(module)s =====> %(message)s",
                    datefmt= "%d-%m-%Y %H:%M"
                    )
logger= logging.getLogger()
