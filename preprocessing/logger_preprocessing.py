import logging
from config import log_folder, log_file_prep
import os

logfolder = os.getcwd() + '\\' + log_folder

logging.basicConfig(
    level=logging.INFO,
    filename=os.path.join(log_folder, log_file_prep),
    format="%(asctime)s - %(levelname)s - %(message)s",
)
