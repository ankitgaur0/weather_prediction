import pandas as pd
import numpy as np
import os,sys
from pathlib import Path
import pickle

#another library
from src.Logger import logging
from src.Exception_handler import Custom_Exception
from src.component.Data_Ingestion import Data_Ingestions
from src.component.Data_Transformer import Data_Transformation



def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            pickle.dump(obj,file_obj)
    except Exception as e:
        logging.info("Exception is occured in utils file")
        raise Custom_Exception(e,sys)