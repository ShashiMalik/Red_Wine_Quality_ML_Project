import os
import pandas as pd
from mlproject_template import logger
from sklearn.model_selection import train_test_split
from mlproject_template.entity.config_entity import DataTransformationConfig




class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)

        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, 'train.csv'),index= False)
        test.to_csv(os.path.join(self.config.root_dir, 'test.csv'), index=False)

        logger.info('Splitted data into training and test')
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
