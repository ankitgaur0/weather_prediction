import os,sys
from pathlib import Path
import pickle
import pandas as pd
import numpy as np

from src.Logger import logging
from src.Exception_handler import Custom_Exception
from src.Utils import load_object

class test_pipeline:
    def __init__(self):
        pass

    def predict_target(self,input_features):
        try:
            preprocessor_obj_path=os.path.join("artifacts","transformation.pkl")
            model_obj_path=os.path.join("artifacts","model.pkl")

            logging.info("loding the transfomation obj and model object")
            preprocessor_obj=load_object(preprocessor_obj_path)
            model_obj=load_object(model_obj_path)

            #now perform the feature engineering on top given data
            scaled_data=preprocessor_obj.transform(input_features)
            #now predict the output from the scaled input features
            pred_value=model_obj.predict(scaled_data)

            return(pred_value)
        except Exception as e:
            raise Custom_Exception(e,sys)
        

class Custom_data:
    def __init__(self,
                 Temperature : float,
                 Humidity : int,
                 Wind_Speed : float,
                 Precipitation : float,
                 Cloud_Cover : str,
                 Atmospheric_Pressure : float,
                 UV_Index : int ,
                 Season : str,
                 Visibility_km : float,
                 Location : str):
        self.Temperature=Temperature
        self.Humidity=Humidity
        self.Wind_Speed=Wind_Speed
        self.Precipitation=Precipitation
        self.Cloud_Cover=Cloud_Cover
        self.Atmospheric_Pressure=Atmospheric_Pressure
        self.UV_Index=UV_Index
        self.Season=Season
        self.Visibility_km=Visibility_km
        self.Location=Location

    def get_data_DataFrame(self):
        try:
            columns_names=['Temperature', 'Humidity', 'Wind Speed', 'Precipitation (%)','Cloud Cover', 'Atmospheric Pressure', 'UV Index', 'Season','Visibility (km)', 'Location']

            data_vales=[self.Temperature, self.Humidity, self.Wind_Speed, self.Precipitation,self.Cloud_Cover, self.Atmospheric_Pressure, self.UV_Index, self.Season,self.Visibility_km, self.Location]

            #now making the data frame
            logging.info("for testing data making the DataFrame ")
            custom_DataFrame=pd.DataFrame(data=[data_vales],columns=columns_names)
            logging.info(f"created dataFrame for the testing data is successfull, the data frame is :\n {custom_DataFrame.head()}")

            return (custom_DataFrame)



        except Exception as e:
            raise Custom_Exception(e,sys)