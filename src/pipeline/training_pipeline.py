import os, sys
from pathlib import Path

from src.component.Data_Ingestion import Data_Ingestions
from src.component.Data_Transformer import Data_Transformation
from src.component.Model_Trainer import Model_Trainer
from src.Logger import logging
from src.Exception_handler import Custom_Exception



try:
    logging.info("trainig pipeline is starting")
    Data_Ingestions_object=Data_Ingestions()
    train_data_path,test_data_path=Data_Ingestions_object.initiate_data()
    logging.info("getting the data from Data_Ingestion is completed")
    #now making the object of the Data Transformer to transfom the data
    logging.info("passing the parameter to Data_transformer is start")
    Data_Transformation_object=Data_Transformation()
    train_array,test_array=Data_Transformation_object.initiate_data_transformer(train_data_path,test_data_path)
    logging.info("completed the passing the data to Data_Transformer module")
    #now making the object of the model trainer
    logging.info("passing the data to model_trainer model is start")
    Model_trainer_object=Model_Trainer()
    Model_trainer_object.initate_model(train_array,test_array)
    logging.info("completed the passing the data to Model_Trainer")
except Exception as e:
    raise Custom_Exception(e,sys)