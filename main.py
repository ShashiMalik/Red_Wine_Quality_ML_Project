from mlproject_template import logger
from mlproject_template.pipepline.stage_01_dat_ingestion import DataIngestionTrainingPipeline
from mlproject_template.pipepline.stage_02_data_validation import DataValidationTrainingPipeline
from mlproject_template.pipepline.stage_03_data_transformation import DataTransformationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<< ")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<< ")
except Exception as e:
    raise e


STAGE_NAME = "DATA_VALIDATION_STAGE"
try:
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<< ")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<< ")
except Exception as e:
    raise e



STAGE_NAME = "DATA_TRANSFORMATION_STAGE"
try:
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<< ")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<< ")
except Exception as e:
    raise e




