from os import getcwd
from .path_tools import readable_path


class Input_files:
    """This class manager the operations about read files"""
    def __init__(self, input_path=getcwd()):
        """Init class, if the path is not given then the current
        working path is taken
        
        Keyword Arguments:
            input_path {string} -- The path to read into (default: {getcwd()})
        """
        self._input_path = input_path + "/"

    @readable_path
    def read_archive(self, name_archive):
        """Reads a file
        
        Arguments:
            name_archive {string} -- The name of the file to read
        """
        with open(self._input_path + name_archive, "r") as archive:
            for line in archive:
                print(line)

    def set_input_path(self, new_input_path):
        """Change the base path
        
        Arguments:
            new_input_path {string} -- The new full path to read into
        """ 
        self._input_path = new_input_path