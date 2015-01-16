import unittest
from celty import conf

CONFIGURATION = "tests/celty.conf"

class TestConfigurationReaderExists(unittest.TestCase):
    def test_loadConfReader(self):
        conf.ConfReader(CONFIGURATION)

class TestConfigurationReader(unittest.TestCase):
    def setUp(self):
        self.reader = conf.ConfReader(CONFIGURATION)

class TestConfigurationReaderErrors(unittest.TestCase):
    def setUp(self):
        self.reader = conf.ConfReader(CONFIGURATION)

    def test_invalidMiyukiPath(self):
        self.assertRaises(IOError, conf.ConfReader, ('lolinvalid.conf'))

    def test_dataAreImportedCorrectly(self):
        try:
            self.assertRaises(AttributeError, self.reader.miyuki_data)
            self.assertTrue(False)
        except:
        	self.assertNotEqual(self.reader.miyuki_data, None)
        	self.assertEqual(self.reader.miyuki_data["notifications"], {"enabled": True})