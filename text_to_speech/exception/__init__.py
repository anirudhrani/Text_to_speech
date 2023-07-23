import os, sys

def error_detail(error_message, sys: sys):
    _, _, exc_tb= sys.exc_info()
    # exc_tb -> Gives the traceback of the error.
    # .tb_frame -> Gives the trace back and the absolute path with 2 slashes.
    # .f_code -> Give the trace back and the absolute path in a proper format (with 1 slash).
    # .co_filename -> Gives the absolute path of the traceback in a proper fromat.
    file_path= os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    error_message= f"Error in script: {file_path}\nAt Line no.: {exc_tb.tb_lineno} \nMessage: {str(error_message)}"
    return error_message

class tts_exception(Exception):
    
    def __init__(self, error_message, sys: sys):
        # super.__init__(error_message)
        self.error_message = error_detail(error_message= error_message, sys= sys)

    def __str__(self):
        return self.error_message