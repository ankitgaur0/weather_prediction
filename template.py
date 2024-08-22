#this is use for creating the structure of the pipeline of the project
import os,sys
from pathlib import Path
import logging

log_format="[%(asctime)s] %(levelname)s - %(name)s - %(filename)s:%(lineno)d - %(message)s"
logging.basicConfig(level=logging.INFO,
                    format=log_format,    # Apply the custom log format
                    datefmt="%Y-%m-%d %H:%M:%S" #custom data format
)

files_names_list=[
    "notebook/__init__.py",
    "notebook/Data",
    "notebook/EDA.ipynb",
    "notebook/model_trainer.ipynb",
    "src/__init__.py",
    "src/component/__init__.py",
    "src/component/Data_Ingestion.py",
    "src/component/Data_Transformer.py",
    "src/component/Model_Trainer.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/test_pipeline.py",
    "src/Logger.py",
    "src/Exception_handler.py",
    "src/Utils.py",
    "test.py",
    'app.py'

]

for file_path in files_names_list:
    logging.info("start to create structure of the project")
    file_path=Path(file_path)
    #now need to have, spilt the file_names so that make the directory
    file_dir,file_name=os.path.split(file_path)

    if (file_dir !=""):
        os.makedirs(file_dir,exist_ok=True)
        logging.info("completing the process of making path(structre)")


    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) ==0):
        with open(file_path,'w') as file_path_obj:
            pass

    else:
        print("file is already present")
        logging.info("file is already present, so leave it")