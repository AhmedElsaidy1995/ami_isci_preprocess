import codecs
import os
#import utils

def get_project_dir():
    """
    Get project path
    :return: current path
    """
    current_dir = os.path.abspath(os.path.dirname(__file__))
    return current_dir