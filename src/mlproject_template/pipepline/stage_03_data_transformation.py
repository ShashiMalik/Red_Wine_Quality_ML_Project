from mlproject_template.config.configuration import ConfigurationManager
from mlproject_template.components.data_transformation import DataTransformation
from mlproject_template import logger

STAGE_NAME = "DATA_TRANSFORMATION_STAGE"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"),'r') as f:
                status = f.read().split(" ")[-1]

                if status == "True":
                    config = ConfigurationManager()
                    data_transformation_config = config.get_data_transformation_config()
                    data_transformation =  DataTransformation(config = data_transformation_config)
                    data_transformation.train_test_spliting()

                else:
                    raise Exception("Your Data Schema is not valid")
        
        except Exception as e:
            print(e)


                    

