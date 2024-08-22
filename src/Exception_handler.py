#here we create our custom exception handing class

import os,sys
from pathlib import Path
class Custom_Exception(Exception):
    def __init__(self,error_message,error_details:sys):
        self.error_message=error_message

        _,_,exc_tb=error_details.exc_info()

        self.line_number=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename


    def __str__(self):
        return "the error find in file name [{0}] and line number is [{1}] \n the error message is [{2}]".format(self.file_name,self.line_number,str(self.error_message))
    


if __name__=="__main__":
    try:
        a=int(input("enter a number for dividing the number"))
        b=10
        print(b/a)
    
    except Exception as e:
        raise Custom_Exception(e,sys)