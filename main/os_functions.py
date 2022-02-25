import os
import urllib.parse
from . import helper_functions

DEFAULT_PATH = os.getenv('WINDIR')


def get_files(path=None):
    files = os.listdir(path)
    file_with_ext = list()
    for file in files:
        file_path = os.path.join(path, file)
        safe_file_path = urllib.parse.quote_plus(file_path)
        file_type = 'dir' if os.path.isdir(file_path) else helper_functions.guess_type(file_path)
        data = {
            'name': file,
            'path': safe_file_path,
            'type': file_type
        }
        file_with_ext.append(data)
    return file_with_ext

