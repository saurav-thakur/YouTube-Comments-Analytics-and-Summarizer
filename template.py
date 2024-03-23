import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s] : %(message)s')

project_name = "youtube_analytics"

list_of_files = [
    # components
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py", #to push the model to cloud
    

    # configuration
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/s3_operations.py",
    
    # constants
    f"{project_name}/constants/__init__.py",
    
    # entity
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/entity/config_entity.py",

    # exception
    f"{project_name}/exception/__init__.py",

    # logger
    f"{project_name}/logger/__init__.py",

    # pipeline
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/train_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",

    # utils
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/utils.py",

    # ml model
    f"{project_name}/ml/__init__.py",
    f"{project_name}/ml/model.py",

    # additional files
    "setup.py",
    "app.py",
    "demo.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
]


for filepath in list_of_files:
    filepath = Path(filepath)

    filedir,filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if not (os.path.exists(filepath)) or os.path.getsize(filepath) == 0:
        os.system(f"touch {filepath}")
        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists!!")