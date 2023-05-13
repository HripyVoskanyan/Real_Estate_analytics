import logging
from config import log_folder, log_file_scrap
import os

logfolder = os.getcwd() + '\\' + log_folder
if not os.path.exists(logfolder):
    os.makedirs(logfolder)

logging.basicConfig(
    level=logging.INFO,
    filename=os.path.join(logfolder, log_file_scrap),
    format="%(asctime)s - %(levelname)s - %(message)s",
)
