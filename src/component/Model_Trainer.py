import os,sys
from pathlib import Path
import pandas as pd
import numpy as np
from dataclasses import dataclass

#some local libraries
from src.Logger import logging
from src.Exception_handler import Custom_Exception
from src.component.Data_Ingestion import Data_Ingestions
from src.component.Data_Transformer import Data_Transformation
#form utils functions 
from src.Utils import save_object

#some framework for making model
import tensorflow
from tensorflow import keras
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

@dataclass
class ModelConfig:
    model_cofig_path:str=os.path.join("artifacts","model.pkl")


class Model_Trainer:
    def __init__(self):
        self.model_obj=ModelConfig()

    def initate_model(self,train_array,test_array):
        try:
            logging.info("starting the process of trainig model ")
            logging.info("spliting the dependent and independent data")
            #spliting the data in the dependent and independent data from the train and test array
            X_train,y_train,X_test,y_test=(
                train_array[:,:18],
                train_array[:,18:22],
                test_array[:,:18],
                test_array[:,18:22]
             )
            #making the dataframe of this 
            logging.info("spliting the data is completed in the X_train and X_test and y_train an y_test data")
            logging.info("using the artifical neural network ")

            model=Sequential()
            model.add(Dense(64,activation="relu",input_shape=(18,)))
            model.add(Dense(32,activation="relu"))
            model.add(Dense(32,activation="tanh"))
            model.add(Dense(16,activation="relu"))
            model.add(Dense(8,activation="relu"))
            model.add(Dense(4,activation="softmax"))

            #store the summary of the model in the logging
            logging.info(f"the summary of the model is :\n {model.summary()}")
            optimizer="adam"
            loss_function="categorical_crossentropy"
            metrics="accuracy"
            #compile the model
            model.compile(optimizer=optimizer,loss=loss_function,metrics=[metrics])
            #just check
            print("="*40)
            print("X_train_data_shape =",X_train.shape)
            print("y_train_data_shape =",y_train.shape)
            print("X_test_data_shape =",X_test.shape)
            print("y_test_data_shape =",y_test.shape)
            print("=" * 40)


            #now fit the data in the model
            history=model.fit(X_train,y_train,epochs=25,validation_data=(X_test,y_test))

            print("the model name is Artifical Neural Network \n activation used = relu and tanh,\n optimzer used =",optimizer,
                  "\n loss function is used =",loss_function,
                  "\n metrics is used to evaluate =",metrics,
                  "\n number of epochs =",25)

            for epoch in range(len(history.history['loss'])):
                log_message = (
                    f"Epoch {epoch + 1}: ",
                    f"loss = {history.history['loss'][epoch]} ",
                    f"accuracy = {history.history['accuracy'][epoch]}"
                )
                # Check if you also have validation data
                if 'val_loss' in history.history:
                    log_message = (
                        f", val_loss = {history.history['val_loss'][epoch]}, "
                        f"val_accuracy = {history.history['val_accuracy'][epoch]}"
                    )

            #now save the object
            print("saving the model in the pickle form")
            logging.info("saving the model in the .pickle form")
            save_object(self.model_obj.model_cofig_path,model)
            logging.info("saved the model in the .pickle form")
            print("saved the model in the pickle form")



        except Exception as e:
            raise Custom_Exception(e,sys)
