import os
import urllib.request as request
import zipfile
from mlproject_template import  logger
from mlproject_template.utils.common import get_size
from mlproject_template.entity.config_entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
                )
            logger.info(f"{filename} download the following info: \n{headers}")

        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))} already exists.")


    def extract_zip_file(self):
        """
        zip_file_path: str
        Extract zip file into the data directory
        funtion returns none 
        """
        unzip_path = self.config.unzip_dir 
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as   zip_ref:
            zip_ref.extractall(unzip_path)


