from src.CardVista.config.configuration import ConfigurationManager
from src.CardVista.components.data_transformation_and_clustering import DataTransformationandClustering
from src.CardVista.logging import logger
from pathlib import Path



STAGE_NAME = "Data Transformation and Cluster Generation stage"

class DataTransformationandClusteringPipeline:
    def __init__(self):
        pass


    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]

            if status == "True":
                config = ConfigurationManager()
                data_transformation_and_clustering_config = config.get_data_transformation_and_clustering_config()
                data_transformation_and_clustering = DataTransformationandClustering(config=data_transformation_and_clustering_config)
                data_transformation_and_clustering.data_transformation_and_clustering()

            else:
                raise Exception("You data schema is not valid")

        except Exception as e:
            print(e)


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationandClusteringPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e