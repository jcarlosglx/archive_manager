from os import getcwd
from .path_tools import writable_path, get_new_name
from os.path import exists


class Output_files:
    """This class manager the operations about output files"""        
    def __init__(self, output_path=getcwd()):
        """Init class, if the path is not given then the current
        working path is taken
        
        Keyword Arguments:
            output_path {string} -- The path to write into
            (default: {getcwd()})
        """
        self._output_path = output_path + "/"
        self._last_file_create = ""

    @writable_path
    def create_new_file(self, name):
        """Create a file (if the file exists then it will be overwritten)
        
        Arguments:
            name {string} -- The name of the file
        """
        self._last_file_create = self._output_path + name
        with open(self._last_file_create, "w") as archive:
            pass

    @writable_path
    def checkout_and_create(self, name):
        """Create a file (if the file exists then it will add a number:
        starting in 0, then 1, then 2, ... until there is a valid file name
        
        Arguments:
            name {string} -- The name of the file
        """
        if exists(self._output_path + name):
            self._last_file_create = get_new_name(self._output_path, name)

            with open(self._output_path + self._last_file_create, "w") \
                    as archive:
                pass
        
        else:
            self._last_file_create = name
            with open(self._output_path + name, "w") as archive:
                pass

    def set_output_path(self, new_output_path):
        """Change the output path
        
        Arguments:
            new_output_path {string} -- The new full path to write into
        """
        self._output_path = new_output_path

    @writable_path
    def add_info_file(self, info, path):
        """Add info at the last line of the file
        
        Arguments:
            info {string} -- The info to write into the path
            path {string} -- The path to write into
        """
        with open(self._output_path + path, "a") as archive:
            archive.write(info)

    @writable_path
    def add_info_last_file_create(self, info):
        """Add info at the last line of the file
        
        Arguments:
            info {string} -- The info to write into the last
            path created
        """        
        with open(self._last_file_create, "a") as archive:
            archive.write(info)
