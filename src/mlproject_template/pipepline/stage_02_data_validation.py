from mlproject_template.config.configuration import ConfigurationManager
from mlproject_template.components.data_validation import DataValidation
from mlproject_template import logger

STAGE_NAME = "DATA_VALIDATION_STAGE"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.Validate_all_columns()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<< ")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<< ")
    except Exception as e:
        raise e

                    

