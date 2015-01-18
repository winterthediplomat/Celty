import unittest
from celty import conf
from celty import communicator as comm
import subprocess
import shlex
import time

CONFIGURATION = "tests/celty.conf"
ARIA_HOST = 'localhost'
ARIA_PORT = 6800
ARIA2C_PATH = '/home/alfateam/aria2-1.18.8-win-32bit-build1/aria2c.exe'

class TestAriaCommunicatorCreation(unittest.TestCase):
    def test_createCommunicator(self):
        self.aria_rpc = comm.AriaCommunicator(ARIA_HOST, ARIA_PORT)

class TestAriaRunning(unittest.TestCase):
    def setUp(self):
        self.aria_spawner = comm.AriaSpawner(ARIA2C_PATH)
        self.aria_rpc = comm.AriaCommunicator(ARIA_HOST, ARIA_PORT)

    def test_isRunning(self):
        please_kill_aria = False
        try:
            self.aria_spawner.spawn(ARIA_PORT)
            time.sleep(1) #wait 1 seconds for let it spawn correctly
            self.assertEqual(self.aria_rpc.isRunning(), True)
            please_kill_aria = True

            self.aria_spawner.kill()
            time.sleep(1) #wait 1 seconds for let it terminate correctly
            self.assertEqual(self.aria_rpc.isRunning(), False)
            please_kill_aria = False
        finally:
            if please_kill_aria:
                self.aria_spawner.kill() #in case of errors, we'll kill it.

