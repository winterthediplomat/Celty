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
