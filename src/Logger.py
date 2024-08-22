# here we define the logging which helps to log the information
import os, sys
from pathlib import Path
import logging
from datetime import datetime

log_file_name=f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
#Logs is the file name where logs info will be store
log_path=os.path.join(os.getcwd(),"Logs",log_file_name)
os.makedirs(log_path,exist_ok=True)

Log_file_path=os.path.join(log_path,log_file_name)  

log_format="[%(asctime)s] %(levelname)s - %(name)s - %(filename)s:%(lineno)d - %(message)s"

logging.basicConfig(
    filename=Log_file_path,
    level=logging.INFO,
    format=log_format

)