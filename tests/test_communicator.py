import unittest
from celty import conf
from celty import communicator as comm
import time
from pyaria2 import PyAria2

CONFIGURATION = "tests/celty.conf"
ARIA_HOST = 'localhost'
ARIA_PORT = 6800
ARIA2C_PATH = '/home/alfateam/aria2-1.18.8-win-32bit-build1/aria2c.exe'

class TestAriaCommunicatorCreation(unittest.TestCase):
    def test_createCommunicator(self):
        self.aria_rpc = comm.AriaCommunicator(port=9999, useRPCSecret=True, fixedSecret="ABCDEF")
        #this is just to check AriaCommunicator object works
        self.aria_rpc.ariaObj.shutdown() 

class TestAriaRunning(unittest.TestCase):
    def setUp(self):
        self.aria_rpc = comm.AriaCommunicator(port=6969,
                                              useRPCSecret=True,
                                              fixedSecret="ROXASPLS")

    @unittest.skip("moved this kind of tests to pyaria2")
    def test_isRunningAndShutdown(self):
        please_kill_aria = False
        try:
            time.sleep(3) #wait 1 seconds for let it spawn correctly
            #print("should be running...")
            self.assertEqual(self.aria_rpc.isRunning(), True)
            #print("oh, it's running!")

            please_kill_aria = True

            self.aria_rpc.kill()
            time.sleep(3) #wait 1 seconds for let it terminate correctly
            #print("should be dead...")
            self.assertEqual(self.aria_rpc.isRunning(), False)
            #print("oh, it's dead!")
            please_kill_aria = False
        finally:
            #print("please_kill_aria: ", please_kill_aria)
            if please_kill_aria:
                self.aria_rpc.ariaObj.shutdown() #in case of errors, we'll kill it.

