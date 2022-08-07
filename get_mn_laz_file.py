import os
import os.path as path
import requests
import pathlib


class FileHandler:
    def __init__(self, local_cache_dir=None) -> None:
        if local_cache_dir:
            self.local_cache_dir = local_cache_dir
        else:
            home_dir = str(pathlib.Path.home()) or os.environ.get("HOME") or os.environ.get("HOMEPATH") or ""
            if not home_dir:
                raise Exception('No default HOME directory found')
            self.local_cache_dir = os.sep.join([home_dir, '.cache', 'mn_lidar'])

        if not path.exists(self.local_cache_dir):
            print(f"Creating {self.local_cache_dir}")
            try:
                os.makedirs(self.local_cache_dir)
            except Exception as e:
                print(f"Local cache dir: {self.local_cache_dir}")
                raise Exception(f"Error creating directory {self.local_cache_dir}: {e}")

    def exists(self, file_name: str) -> bool:
        return path.exists(os.path.join(self.local_cache_dir, file_name))

    def write(self, file_name: str, contents: bytes) -> None:
        print(4, len(contents))
        fn = os.path.join(self.local_cache_dir, file_name)
        with open(fn, 'wb') as f:
            n = f.write(contents)
            print(f"saved {n} bytes in {fn}")

    def read(self, file_name: str) -> bytes:
        with open(os.path.join(self.local_cache_dir, file_name), 'rb') as f:
            return f.read()

    def get_filename(self, file_name):
        return os.path.join(self.local_cache_dir, file_name)

def get_laz_tile(tilename):  # return a local filename
    file_handler = FileHandler()
    base_url = "https://resources.gisdata.mn.gov/pub/data/elevation/lidar/projects/arrowhead/block_3/laz/"
    if not file_handler.exists(tilename):
        url = base_url + tilename
        r = requests.get(url, timeout=15)
        print('Retrieving {0}'.format(url))
        data = r.content
        print('Retrieved {0} ({1} bytes)'.format(url, len(data)))
        file_handler.write(tilename, data)
    return file_handler.get_filename(tilename)
