import yaml
import logging

class ConfReader(object):
    """
    ConfReader parses Miyuki configuration reader
    """
    def __init__(self, miyuki_conf_file):
        self.miyuki_conf_file = miyuki_conf_file
        self.parseConf()

    def parseConf(self):
        self.miyuki_data = yaml.load(self.miyuki_conf_file)
        logging.debug("parse_conf", self.miyuki_data)

    def extractShowInfo(self, show_name):
        try:
            return [series_data for series_data in self.miyuki_data["series"] 
                       if series_data["name"] == show_name][-1]
        except IndexError:
            #as no element has been found, the show has not been found
            raise ValueError("Show {0} does not exists!".format(show_name))

    def extractShowDownloadInfo(self, show_name):
        try:
            return self.extractShowInfo(show_name)["download"]
        except KeyError:
            #no "download" section has been declared for this show
            #use global definitions
            return self.miyuki_data["download"]

    @property
    def watchDir(self):
        return self.miyuki_data["watchDir"]
    
    @property
    def globalDownloadDir(self):
        return self.miyuki_data["download"]["downloadDir"]

    @property
    def globalSeedTime(self):
        try:
            return self.miyuki_data["download"]["seedTime"]
        except KeyError:
            return 0
    
    def downloadDir(self, show_name):
        return self.extractShowDownloadInfo(show_name)["downloadDir"]

    def seedTime(self, show_name):
        try:
            return self.extractShowDownloadInfo(show_name)["seedTime"]
        except KeyError:
            return self.globalSeedTime

    @property
    def aria2Host(self):
        try:
            return self.miyuki_data["download"]["aria2"]["aria2Host"]
        except KeyError:
            return "localhost"

    @property
    def aria2Port(self):
        try:
            return self.miyuki_data["download"]["aria2"]["aria2Port"]
        except KeyError:
            return 6800

    @property
    def aria2UseSecret(self):
        try:
            return self.miyuki_data["download"]["aria2"]["useRPCSecret"]
        except KeyError:
            return True #by default, we'll use RPC secrets. muh security. 

    @property
    def aria2FixedRPCSecret(self):
        try:
            return self.miyuki_data["download"]["aria2"]["fixedRPCSecret"]
        except KeyError:
            return None

    @property
    def series_names(self):
        return [show["name"] for show in self.miyuki_data["series"]]
    
        
