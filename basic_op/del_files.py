from os.path import isfile, isdir
from fnmatch import filter as fnm_filter
from shutil import rmtree
from os import walk, remove, rmdir
from .path_tools import validate_path
from .error_file import error_is_not_dir, error_is_not_file


class Delete_files:
    """This class manager the operations about delete files"""
    def __init__(self):
        """Init class
        """
        self._last_del_file = ""
        self._last_del_dir = ""
        self._last_del_type_file = ""

    @validate_path
    def del_file(self, path):
        """Delet a file
        
        Arguments:
            path {string} -- The path of the file to delete
        """
        if isfile(path):
            remove(path)
            self._last_del_file = path
        else:
            error_is_not_file(path)

    @validate_path
    def del_type_files(self, path, pattern="*.txt"):
        """Delete all the files that match the pattern
        
        Arguments:
            path {string} -- The dir to delete into
        
        Keyword Arguments:
            pattern {string} -- The patter to delete
            (default: {"*.txt"})
        """
        for root, subdir, name_files in walk(path):
            for archive in fnm_filter(name_files, pattern):
                remove(path+archive)
        self._last_del_type_file = pattern

    @validate_path
    def del_dir(self, path, del_all=False):
        """Delete a dir
        
        Arguments:
            path {string} -- The path dir to delete
        
        Keyword Arguments:
            del_all {bool} -- Remove empty dir if 'del_all=False'
            remove a dir with items 'change del_all=True' (default: {False})
        """
        if isdir(path):
            if del_all:
                rmtree(path)
            else:
                rmdir(path)
            self._last_del_dir = path
        else:
            error_is_not_dir(path)
