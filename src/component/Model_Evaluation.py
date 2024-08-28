import mlflow
import mlflow.keras
#for getting url
from urllib.parse import urlparse
import os,sys
import numpy as np
import mlflow.tensorflow.autologging
from src.Exception_handler import Custom_Exception
from src.Logger import logging
from src.Utils import load_object
from sklearn.metrics import accuracy_score,classification_report


class Model_Evaluate:
    def __init__(self):
        pass

    def get_eval_metrics(self,actual_values,pred_values):
        print(np.shape(actual_values))
        print(np.shape(pred_values))
        actual_value=np.argmax(actual_values,axis=1)
        pred_value=np.argmax(pred_values,axis=1)
        accuracy=accuracy_score(actual_value,pred_value)
        class_report=classification_report(actual_value,pred_value,output_dict=True)
        return(accuracy,class_report)

    def initiate_data_evaluation(self,test_array):
        try:
            X_test_array=test_array[:,:18]
            y_test_array=test_array[:,18:22]

            model_path=os.path.join("artifacts","model.pkl")
            model=load_object(model_path)

            tracking_url_store=urlparse(mlflow.get_tracking_uri()).scheme

            logging.info("activate the mlflow activation")
            with mlflow.start_run():

                y_pred_values=model.predict(X_test_array)
                #calling the get_eval_metrics for getting metrics
                (accuracy_score,classification_report)=self.get_eval_metrics(y_test_array,y_pred_values)
                mlflow.log_metric("accuracy_score",accuracy_score)
                logging.info("logged the accuracy_score in the mlflow log_metric")
                for class_label, metrics in classification_report.items():
                    if class_label not in ['accuracy', 'macro avg', 'weighted avg']:
                        for metric_name, metric_value in metrics.items():
                            mlflow.log_metric(f"{class_label}_{metric_name}", metric_value)
                logging.info("logged the classification_report for each class in the mlflow log_metrics")


                if tracking_url_store !="file": 
                    mlflow.keras.load_model(model,"ANN model",registered_model_name="artifical_neural_network")

                else:
                    mlflow.keras.log_model(model,"model")

                mlflow.log_param("epochs",25)
                mlflow.log_param("optimizer","adam")
                mlflow.log_param("loss","categorical_crossentropy")
                logging.info("logged the infomation and model in the mlflow keras log_model")

        except Exception as e:
            raise Custom_Exception(e,sys)