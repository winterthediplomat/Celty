import yaml

class ConfReader(object):
    """
    ConfReader parses Miyuki configuration reader
    """
    def __init__(self, miyuki_conf_path):
        self.miyuki_conf_path = miyuki_conf_path
        self.parseConf()

    def parseConf(self):
        self.miyuki_data = yaml.load(open(self.miyuki_conf_path))

    def extractShowDownloadInfo(self, show_name):
        try:
            return [series_data for series_data in self.miyuki_data["series"] 
                       if series_data["name"] == show_name][-1]["download"]
        except IndexError:
            #as no element has been found, the show has not been found
            raise ValueError("Show {0} does not exists!".format(show_name))
        except KeyError:
        	#no "download" section has been declared for this show
        	#use global definitions
        	return self.miyuki_data["download"]

    @property
    def globalDownloadDir(self):
        return self.miyuki_data["download"]["downloadDir"]

    @property
    def globalSeedTime(self):
        return self.miyuki_data["download"]["seedTime"]
    
    def downloadDir(self, show_name):
        return self.extractShowDownloadInfo(show_name)["downloadDir"]

    def seedTime(self, show_name):
        return self.extractShowDownloadInfo(show_name)["seedTime"]
