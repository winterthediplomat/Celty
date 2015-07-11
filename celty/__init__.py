from __future__ import print_function, unicode_literals
import click
from .conf import ConfReader
from .communicator import AriaCommunicator
from .torrent import TorrentFinder, TorrentInfo
import logging
from os.path import expandvars, basename
from os import getenv
logging.basicConfig(filename=expandvars("$HOME/.celty.log"), level=logging.DEBUG)

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
    confReader = ConfReader(miyuki_path)
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

# @main.command()
# def stop():
#     """
#     $ celty stop

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
    communicator = AriaCommunicator("localhost",
                                    port,
                                    True,
                                    secret)

@main.command()
def add(torrentpath):
    """
    adds a torrent in the 
    """
    raise NotImplementedError()


if __name__ == '__main__':
    main()
    
