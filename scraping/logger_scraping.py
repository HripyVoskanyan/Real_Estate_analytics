import logging
from config import log_folder, log_file_scrap
import os


logging.basicConfig(
    level=logging.INFO,
    filename=os.path.join(log_folder, log_file_scrap),
    format="%(asctime)s - %(levelname)s - %(message)s",
)
