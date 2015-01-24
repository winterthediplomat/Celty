import os.path as path
from os import walk
import re

class TorrentInfo(object):
    def __init__(self, series_name, fansub, episode, additionalInfo=None):
        self._fansub      = fansub
        self._episode     = episode
        self._series_name = series_name
        self._additionalInfo = additionalInfo or dict()

    @property
    def additionalInfo(self):
        return self._additionalInfo
    @additionalInfo.setter
    def additionalInfo(self, value):
        self._additionalInfo = value
    
    @property
    def fansub(self):
        return self._fansub
    @fansub.setter
    def fansub(self, value):
        self._fansub = value
    
    @property
    def episode(self):
        return self._episode
    @episode.setter
    def episode(self, value):
        self._episode = value
    
    @property
    def fansub(self):
        return self._fansub
    @fansub.setter
    def fansub(self, value):
        self._fansub = value
    

    @staticmethod
    def patternFromSeriesConf(series_conf):
        try:
            pattern = series_conf["pattern"]
        except KeyError:
            pattern = "[$fansub] $name"

        keys = [k for k in series_conf.keys() if k not in ["pattern", "download"]]
        for key_ in keys:
            try:
                pattern = pattern.replace("$"+key_, series_conf[key_])
            except TypeError:
                pass
        return pattern

    @staticmethod
    def seriesFromPattern(pattern, conf):
        for show_name in conf.series_names:
            show_conf = conf.extractShowInfo(show_name)
            if pattern.startswith(TorrentInfo.patternFromSeriesConf(show_conf)):
                return show_conf
        raise ValueError("No show matching the given pattern has been found")



class TorrentFinder(object):
    def __init__(self, watch_dir):
        self.watch_dir = watch_dir

    def list(self):
        for actDir, dirs, files in walk(self.watch_dir):
            for file_ in files:
                yield path.join(actDir, file_)