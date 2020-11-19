from .basic_op.input_files import Input_files
from .basic_op.output_files import Output_files
from .basic_op.del_files import Delete_files
from os import getcwd


class IO_program(Input_files, Output_files, Delete_files):
    """This class is the manager: input, output and delete files
    
    Arguments:
        Input_files {Class} -- Class from which it inherits
        Output_files {Class} -- Class from which it inherits
        Delete_files {Class} -- Class from which it inherits
    """
    def __init__(self, input_path=getcwd(), output_path=getcwd()):
        """Init the clas
        
        Keyword Arguments:
            input_path {string} -- The path to read into
            (default: {getcwd()})
            output_path {string} -- The path to write into
            (default: {getcwd()})
        """        
        Input_files.__init__(self, input_path)
        Output_files.__init__(self, output_path)
        Delete_files.__init__(self)
