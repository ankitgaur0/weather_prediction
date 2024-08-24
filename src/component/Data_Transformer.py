from src.component.Data_Ingestion import Data_Ingestions
from src.Logger import logging
from src.Exception_handler import Custom_Exception
import os,sys
import pandas as pd
import numpy as np
from dataclasses import dataclass

#some other important library
from sklearn.preprocessing import OneHotEncoder,LabelEncoder,StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
#one extra local library to use save the object in the pickle form
from src.Utils import save_object


@dataclass
class DataTransformer_config:
    transformer_file_path=os.path.join("artifacts","transformation.pkl")

class  Data_Transformation:
    def __init__(self):
        self.transformer_obj=DataTransformer_config()

    def get_data_transformation(self):
        logging.info("now feature engineering is starting to transform the data set")
        try:
            logging.info("data transformation is initiating")
            numerical_colums_names=['Temperature', 'Humidity', 'Wind Speed', 'Precipitation (%)',
       'Atmospheric Pressure', 'UV Index', 'Visibility (km)']
            categorical_columns_names=['Cloud Cover', 'Season', 'Location']

            logging.info("making the pipeline for transformation of the data")

            numerical_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="mean")),
                    ("scaler",StandardScaler())
                ]
            )
            categorical_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most frequent")),
                    ("encoder",OneHotEncoder(sparse_output=False))
                ]
            )
            #now define the ColumnsTransformer
            preproccor=ColumnTransformer(
                [
                    ("numerical_pipeline",numerical_pipeline,numerical_colums_names),
                    ("categorical_pipeline",categorical_pipeline,categorical_columns_names)
                ]
            )

            return (preproccor)

        except Exception as e:
            raise Custom_Exception(e,sys)
        

    #create a new class for transform the data
    def initiate_data_transformer(self,train_data_path,test_data_path):
        try:
            logging.info("read the train and test data in transformer file")
            train_data=pd.read_csv(train_data_path)
            test_data=pd.read_csv(test_data_path)

            logging.info("reading the csv is completed")
            #now log the head values of the train_data and test_data DataFrame in logging file
            logging.info(f"the train data head valus is:\n {train_data.head().to_string()}")
            logging.info(f"the test data head valus is:\n {test_data.head().to_string()}")

            preprocessor_obj=self.get_data_transformation()
            #define the target features in the target_feature variable
            target_feature="Weather Type"

            train_target_data=pd.DataFrame(train_data[target_feature],columns=["Weather Type"])
            #drop the target feature in the train data
            input_train_data=train_data.drop([target_feature],axis=1)
            #now test_target_data
            test_target_data=pd.DataFrame(test_data[target_feature],columns=["Weather Type"])
            input_test_data=test_data.drop([target_feature],axis=1)

            #now fit the input train and test data in the preprocessor obj to tranform the data
            #data should be in array
            input_train_data_array=preprocessor_obj.fit_transform(input_train_data)
            #for validation 
            input_test_data_array=preprocessor_obj.transform(input_test_data)

            #now target feature is a categorical feature, then encode this
            logging.info("encode the target feature")
            ohe=OneHotEncoder(sparse_output=False)
            train_target_data=ohe.fit_transform(train_target_data)
            test_target_data=ohe.fit_transform(test_target_data)
            # np.c_ is used to concate the array 1D ( form ) to array 2D form.
            train_array=np.c_[input_train_data_array,np.array(train_target_data)]
            test_array=np.c_[input_test_data_array,np.array(test_target_data)]
            logging.info("complete the transformation of the data")

            #save the object
            logging.info("saving the preprocessor object")

            # save _object function is created in utils file, firt parameter is file_path and second is object
            save_object(self.transformer_obj.transformer_file_path,obj=preprocessor_obj)
            return (
                train_array,
                test_array
            )
        except Exception as e:
            raise Custom_Exception(e,sys)


