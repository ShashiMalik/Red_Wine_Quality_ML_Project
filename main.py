from mlproject_template import logger
from mlproject_template.pipepline.stage_01_dat_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<< ")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<< ")
except Exception as e:
    raise e

