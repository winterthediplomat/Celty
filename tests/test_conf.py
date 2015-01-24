import unittest
from celty import conf

CONFIGURATION = "tests/celty.conf"

class TestConfigurationReaderExists(unittest.TestCase):
    def test_loadConfReader(self):
        conf.ConfReader(CONFIGURATION)

class TestConfigurationReader(unittest.TestCase):
    def setUp(self):
        self.reader = conf.ConfReader(CONFIGURATION)

    def test_dataAreImportedCorrectly(self):
        try:
            self.assertRaises(AttributeError, self.reader.miyuki_data)
            self.assertTrue(False)
        except:
            self.assertNotEqual(self.reader.miyuki_data, None)
            self.assertEqual(self.reader.miyuki_data["notifications"], {"enabled": True})

    def test_globalDownloadDirIsImportedCorrectly(self):
        self.assertEqual(self.reader.globalDownloadDir, "F:/global_folder")

    def test_globalSeedingTimeIsImportedCorrectly(self):
        self.assertEqual(self.reader.globalSeedTime, 10)

    def test_downloadDirPerSerieIsImportedCorrectly(self):
        self.assertEqual(self.reader.downloadDir("Nisekoi"), "F:/serie_tv/False_Love")
        self.assertEqual(self.reader.downloadDir("Sora no Woto"), "F:/global_folder")

    def test_seedTimePerSerieIsImportedCorrectly(self):
        self.assertEqual(self.reader.seedTime("Shigatsu"), 25)
        self.assertEqual(self.reader.seedTime("Sora no Woto"), 10)

class TestConfigurationReaderErrors(unittest.TestCase):
    def setUp(self):
        self.reader = conf.ConfReader(CONFIGURATION)

    def test_invalidMiyukiPath(self):
        self.assertRaises(IOError, conf.ConfReader, ('lolinvalid.conf'))

    def test_downloadDirPerSerieNotFound(self):
        self.assertRaises(ValueError, self.reader.downloadDir, "RoxasPls")      
        self.assertRaises(TypeError, self.reader.downloadDir)

    def test_seedTimePerSerieNotFound(self):
        self.assertRaises(ValueError, self.reader.seedTime, "RoxasPls")
        self.assertRaises(TypeError, self.reader.seedTime)

