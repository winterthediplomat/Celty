import xmlrpclib
import subprocess
import shlex
from random import choice
from string import ascii_letters as letters

class AriaSpawner(object):
    def __init__(self, aria2c_path):
        self.aria2c_path = aria2c_path

    def spawn(self, port, useSecret=False, givenSecret=None):
        secret = givenSecret
        command = """{0} --enable-rpc=true \
                    --continue=true \
                    --rpc-listen-port={1}""".format(self.aria2c_path, port)
        if useSecret:
            command += " --rpc-secret={0}".format(secret)
        subprocess.Popen(command, shell=True).pid
        return secret

    def kill(self):
        args = shlex.split("killall aria2c")
        subprocess.Popen(args)

class AriaCommunicator(object):
    def __init__(self, host="localhost", port=6800, useRPCSecret=False, fixedSecret=None):
        self.host = host
        self.port = port
        self.useRPCSecret = useRPCSecret
        #print("[AriaCommunicator.__init] use secret: {0}".format(self.useRPCSecret))
        self.secret = "token:{0}".format(fixedSecret or self.generateSecret())
        self.ariaProxy = xmlrpclib.ServerProxy("http://{0}:{1}/rpc".format(host, port))

    def generateSecret(self):
        def gimmeLetters(how_many):
            for i in range(how_many):
                yield choice(letters)

        return "".join(gimmeLetters(15))

    def getVersion(self):
        if self.useRPCSecret:
            return self.ariaProxy.aria2.getVersion(self.secret)
        else:
            return self.ariaProxy.aria2.getVersion()

    def isRunning(self):
        try:
            self.getVersion()
            return True
        except xmlrpclib.socket.error: 
            #if we can't talk to it, it's not running!
            return False

    def addTorrent(self, torrentpath, downloadDir):
        torrent_content = xmlrpclib.Binary(open(torrentpath).read())
        if self.useRPCSecret:
            #TODO: re-add downloadDir
            self.ariaProxy.aria2.addTorrent(self.secret, torrent_content)