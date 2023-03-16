import sys 

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    filename,linenumber = exc_tb.tb_frame.f_code.co_filename,exc_tb.tb_lineno 
    error_msg = "Error occured in python script name [{0}], in line number [{1}], error [{2}]".format(
        filename,linenumber,str(error))
    return error_msg


## overwtiting default Exception class 
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error=error_message, error_detail=error_detail)


    def __str__(self):
        return self.error_message
    
