from pyaria2 import PyAria2
import socket
from random import choice
from string import ascii_letters as letters

class AriaCommunicator(object):
    def __init__(self, host="localhost", port=6800, useRPCSecret=False, fixedSecret=None, globalOptions=None):
        self.host = host
        self.port = port
        #self.useRPCSecret = useRPCSecret
        #print("[AriaCommunicator.__init] use secret: {0}".format(self.useRPCSecret))
        secret = fixedSecret or self.generateSecret()
        #self.rpcSecret = "token:{0}".format(secret)
        rpc_conf = {"useSecret":useRPCSecret, "secret":secret}
        self.ariaObj = PyAria2(self.host, self.port, rpcSecret=rpc_conf)
        if globalOptions:
            self.setGlobalOptions(globalOptions)

    def setGlobalOptions(self, options):
        self.ariaObj.changeGlobalOption(options)

    @staticmethod
    def generateSecret():
        def gimmeLetters(how_many):
            for i in range(how_many):
                yield choice(letters)

        return "".join(gimmeLetters(15))

    def isRunning(self):
        return self.ariaObj.isAria2rpcRunning()

    def kill(self):
        return self.ariaObj.shutdown()

    def addTorrent(self, torrentpath, options):
        return self.ariaObj.addTorrent(torrentpath, options=options)
