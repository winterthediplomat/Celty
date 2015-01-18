import os.path as path
from os import walk

class TorrentFinder(object):
    def __init__(self, watch_dir):
        self.watch_dir = watch_dir

    def list(self):
        for actDir, dirs, files in walk(self.watch_dir):
            for file_ in files:
                yield path.join(actDir, file_)