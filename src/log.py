import logging

# change format string param in function if you want to change output structure of the logs
def logger (data_source, format_string = "%(asctime)s - %(name)s - %(levelname)s\nMessage:%(message)s\nFile: %(filename)s\nFunction: %(funcName)s\nlineNumber: %(lineno)d \n"):

    logging.basicConfig(level=logging.DEBUG, filename=f"./logs/{data_source}/{data_source}.log", filemode="a", format= format_string)

    return logging.getLogger(__name__)

    

