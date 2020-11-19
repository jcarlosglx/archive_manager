def error_not_exist(path):
    print("\nThis path does not exist: {}".format(path))


def error_is_not_file(path):
    print("\nThis is not a file: {}, unable to erase".format(path))


def error_is_not_dir(path):
    print("\nThis is not a dir: {}, unable to erase".format(path))


def error_unreadable_file(path):
    print("\nUnable to read the file: {}".format(path))


def error_unwritable_dir(path):
    print("\nUnable to write in the dir: {}".format(path))
