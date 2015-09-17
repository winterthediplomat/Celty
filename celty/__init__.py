from __future__ import print_function
import click
from .conf import ConfReader, InvalidPropertyError
from .communicator import AriaCommunicator
from .torrent import TorrentFinder, TorrentInfo
import logging
from os.path import expandvars, basename, join
from os import getenv
import json
logging.basicConfig(filename=expandvars("$HOME/.celty.log"), level=logging.DEBUG)
import sys

@click.group()
def main():
    """Where the journey begins..."""
    pass

@main.command()
@click.argument("miyuki-path")
def start(miyuki_path):
    """
    $ celty start miyuki-path

    connects to an aria2c server (starts one up if necessary) and loads
    all the torrents it finds in watch directory
    """
    logging.info("called celty start")
    confReader = ConfReader(open(miyuki_path))
    logging.debug("created confReader, path is {}".format(miyuki_path))
    communicator = AriaCommunicator(confReader.aria2Host,
                                    confReader.aria2Port,
                                    confReader.aria2UseSecret,
                                    confReader.aria2FixedRPCSecret)
    communicator.setGlobalOptions({
            "max-concurrent-downloads":2,
            "check-integrity": True,
            "seed-time": confReader.globalSeedTime
        })
    logging.debug("created communicator")
    torrentFinder = TorrentFinder(confReader.watchDir)
    logging.debug("created torrent finder, watch dir is {}".format(confReader.watchDir))
    logging.debug("torrents found: {}".format(len(list(torrentFinder.list()))))
    for file_ in torrentFinder.list():
        file_torrentname = basename(file_)
        try:
            seriesConf = TorrentInfo.seriesFromPattern(file_torrentname, confReader)
            downloadFolder = confReader.downloadDir(seriesConf["name"])
            seedingTime = confReader.seedTime(seriesConf["name"])
        except ValueError: #it should not happen, but never say never...
            downloadFolder = confReader.globalDownloadDir
            seedingTime = confReader.globalSeedTime
            logging.info("couldn't find a series from {}, defaulting to {}".format(file_, downloadFolder))
        logging.info("torrent {0} will be added at path {1}".format(file_, downloadFolder))
        torrent_id = communicator.addTorrent(file_, {"dir":downloadFolder, "seed-time":seedingTime})
        logging.info("torrent {0} has gid {1}".format(file_, torrent_id))

#@main.command()
#def stop():
#    """
#    $ celty stop
#
#     stops the aria2c server specified.
#     """
#     logging.info("called celty stop")
#     confReader = ConfReader(miyuki_path)
#     logging.debug("created confReader, path is {}".format(miyuki_path))
#     communicator = AriaCommunicator(confReader.aria2Host,
#                                     confReader.aria2Port,
#                                     confReader.aria2UseSecret,
#                                     confReader.aria2FixedRPCSecret)
#     logging.debug("created communicator")
#     communicator.kill()

@main.command()
def start_aria(port=6969, secret="celtyftw"):
    """
    starts aria2
    """
    logging.info("called `celty start_aria`")
    communicator = AriaCommunicator("localhost",
                                    port,
                                    True,
                                    secret)

@main.command()
@click.argument("miyuki_path")
@click.argument("torrent_path")
def add(miyuki_path, torrent_path):
    """
    adds a torrent to the aria2 daemon to be downloaded.
    """
    internal_add(miyuki_path, torrent_path)


def internal_add(miyuki_path, torrent_path):
    logging.info("called `celty add {0} {1}`".format(miyuki_path, torrent_path))
    confReader = ConfReader(open(miyuki_path))
    logging.debug("created confReader, path is {}".format(miyuki_path))
    communicator = AriaCommunicator(confReader.aria2Host,
                                    confReader.aria2Port,
                                    confReader.aria2UseSecret,
                                    confReader.aria2FixedRPCSecret)
    logging.debug("created communicator")
    torrent_path = join(confReader.watchDir, torrent_path)
    
    try:
        seriesConf = TorrentInfo.seriesFromPattern(file_torrentname, confReader)
        downloadFolder = confReader.downloadDir(seriesConf["name"])
    except ValueError:
        downloadFolder = confReader.globalDownloadDir

    torrent_id = communicator.addTorrent(torrent_path+".torrent", {"dir":downloadFolder})
    logging.info("added torrent {0} to aria2".format(torrent_id))

@main.command()
@click.argument("miyuki_path")
@click.argument("variable")
def get(miyuki_path, variable):
    """
    please note that the variable must be the same you modify in the conf!
    for now, it works only for global variables.
    
    e.g: if you want to know if notifications are enabled, ask `celty get notifications.enabled`.
         for the watchdir path, ask `celty get watchDir`

    return code is 1 if Celty cannot find the value in the configuration.
    """
    try:
        print(internal_get(miyuki_path, variable), end="")
    except InvalidPropertyError:
        sys.exit(1)

def internal_get(miyuki_path, variable):
    confReader = ConfReader(open(miyuki_path))
    return confReader.propertyByName(variable)


if __name__ == '__main__':
    main()
    
