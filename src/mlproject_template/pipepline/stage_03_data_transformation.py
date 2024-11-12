from mlproject_template.config.configuration import ConfigurationManager
from mlproject_template.components.data_transformation import DataTransformation
from mlproject_template import logger

STAGE_NAME = "DATA_TRANSFORMATION_STAGE"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation =  DataTransformation(config = data_transformation_config)
        data_transformation.train_test_spliting()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<< ")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<< ")
    except Exception as e:
        raise print(e)

                    

