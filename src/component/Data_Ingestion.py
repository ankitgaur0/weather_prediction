import os,sys
from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.Logger import logging
from src.Exception_handler import Custom_Exception

@dataclass
class Data_ingest_config:
    raw_data_path: str =os.path.join("artifacts","raw_data.csv")
    train_data_path: str =os.path.join("artifacts","train_data.csv")
    test_data_path: str =os.path.join("artifacts","test_data.csv")

class Data_Ingestions:
    def __init__(self) -> None:
        self.data_config=Data_ingest_config()
    def initiate_data(self):
        logging.info("now start to initiate the data")
        try:
            #first load the data by pandas in variable df
            data=pd.read_csv(Path(os.path.join(r"D:/weather/notebook/Data","weather_classification_data.csv")))
            logging.info("ingestion of data is completed")
            #now store the raw data into artifacts raw_data_path folder
            os.makedirs(os.path.join(os.path.dirname(self.data_config.raw_data_path)),exist_ok=True)
            data.to_csv(self.data_config.raw_data_path)
            logging.info("raw data is successfully store in the artifact folder")


            #now spilt the data into two category train and test
            logging.info("spiliting the data in train and test category")
            train_data,test_data=train_test_split(data,test_size=0.30)
            #now making the directory and store the data successfully.
            os.makedirs(os.path.join(os.path.dirname(self.data_config.train_data_path)),exist_ok=True)
            os.makedirs(os.path.join(os.path.dirname(self.data_config.test_data_path)),exist_ok=True)

            #now store the data succesfully
            train_data.to_csv(self.data_config.train_data_path)
            test_data.to_csv(self.data_config.test_data_path)
            logging.info("store the data into arifacts train and test data is completed")
            logging.info("return the train and test data_path by this function")
            return(
                self.data_config.train_data_path,
                self.data_config.test_data_path
            )



        except Exception as e:
            raise Custom_Exception(e,sys)
        

        if __name__=="__main__":
            obj=Data_Ingestion()
            train,test=obj.initiate_data()
            print(train,test)