'''
Create a logging framework to collect all the logs into a single file .Please follow all the tasks below.

 - Make the logger customisable, with settings being retrieved from a configuration file
 - Create the logging framework; every time the logger is invoked, it should log into a single file
 - The logging format has to be generic with the module_name, function_name, line_no : message
'''

import os
import logging.config
import functools
import yaml
from src.logexception.exceptionhandler import ApplicationException

def get_logger():

    """ Setup logging configuration """

    ''' Setting the config path for logging configuration YML '''
    config_path = os.path.join(os.path.dirname(__file__), '../../resources/log_config.yml')

    path = config_path
    value = os.getenv('LOG_CFG', None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=logging.INFO)
    return logging

def application_exception(function):
    """ A decorator that wraps the passed in function and logs exceptions """

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        logger = get_logger()
        try:
            return function(*args, **kwargs)
        except ApplicationException as ex:
            # log the exception
            err = "There was an exception inside module ["
            err += function.__module__+'], '
            err += 'function [' +function.__name__+'] with error message: '
            err += ex.message
            logger.error(err)

    return wrapper