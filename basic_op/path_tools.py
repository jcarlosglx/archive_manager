from .error_file import error_not_exist, error_unreadable_file, \
    error_unwritable_dir
from os.path import exists, isdir, isfile
from datetime import datetime


def validate_path(function):
    """Given a function, check a if the path exists
    
    Arguments:
        function {function(obj, string)} -- A function with an object
        and a string path
    
    Raises:
        FileExistsError: If the file or the path does not exist
    
    Returns:
        function -- The given function
    """
    def check_path(obj, path_to_check, *others):
        if exists(path_to_check):
            return function(obj, path_to_check, *others)
        else:
            error_not_exist(path_to_check)
            raise FileNotFoundError
    return check_path


def get_new_name(path, old_name):
    """Given a file name return the name plus a number: starting in 0, then 1,
    then 2, ... until there is a valid file name
    
    Arguments:
        old_name {string} -- Name of the file
    
    Returns:
        string -- Name of the file plus the current time
        (name_day_hour_minute_second_microsecond)
    """
    index = old_name.find(".")
    number = 0
    str_number = "_" + str(number)
    new_name = old_name[:index] + str_number + old_name[index:]
    while exists(path + new_name):
        number += 1
        str_number = "_" + str(number)
        new_name = old_name[:index] + str_number + old_name[index:]
    return new_name


def writable_path(function):
    """Given a function, check a if the path is writable
    
    Arguments:
        function {function(obj, string)} -- A function with an object
        and a string path
    
    Raises:
        FileExistsError: If the file or the path does not exist
    
    Returns:
        function -- The given function
    """
    def check_dir(obj, path_to_check, *others):
        if exists(obj._output_path):
            if isdir(obj._output_path):
                return function(obj, path_to_check, *others)
            else:
                error_unwritable_dir(obj._output_path)
                raise FileNotFoundError
        else:
            error_not_exist(obj._output_path)
            raise FileNotFoundError
    return check_dir


def readable_path(function):
    """Given a function, check a if the path is readable
    
    Arguments:
        function {function(obj, string)} -- A function with an object
        and a string path
    
    Raises:
        FileExistsError: If the file or the path does not exist
    
    Returns:
        function -- The given function
    """
    def check_file(obj, path_to_check, *others):
        path = obj._input_path + path_to_check
        if exists(path):
            if isfile(path):
                return function(obj, path_to_check, *others)
            else:
                error_unreadable_file(path)
                raise FileNotFoundError
        else:
            error_not_exist(path)
            raise FileNotFoundError
    return check_file
