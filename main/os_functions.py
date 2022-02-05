import os
import mimetypes
import urllib.parse
DEFAULT_PATH = os.getenv('WINDIR')


def get_files(path=None):
    files = os.listdir(path)
    file_with_ext = list()
    for file in files:
        file_path = os.path.join(path, file)
        safe_file_path = urllib.parse.quote_plus(file_path)
        type = 'dir' if os.path.isdir(file_path) else mimetypes.guess_extension(file_path)
        data = {
            'name': file,
            'path': safe_file_path,
            'type': type
        }
        file_with_ext.append(data)
    return file_with_ext

