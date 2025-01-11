# ==============================================================================================
#   Description: This module contains general functions that aid in the processing of data sets
# ==============================================================================================

import os


def refactor_path(file_path):
    """This function sets the path connectors depending on the current os"""
    
    if os.name == 'posix': # Unix (Linux and MacOS)
        file_path = file_path.replace('\\', '/')
    else: # Windows
        file_path = file_path.replace('/', '\\')
    
    return file_path