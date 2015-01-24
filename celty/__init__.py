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
    confReader = ConfReader(miyuki_path)
    communicator = AriaCommunicator(confReader.aria2Host,
                                    confReader.aria2Port,
                                    confReader.aria2UseSecret,
                                    confReader.aria2FixedRPCSecret)
    torrentFinder = TorrentFinder(confReader.watchDir)
    for file_ in torrentFinder.list():
        file_torrentname = basename(file_)
        try:
            downloadFolder = confReader.downloadDir(TorrentInfo.seriesFromPattern(file_torrentname, confReader)["name"])
        except ValueError: #it should not happen, but never say never...
            downloadFolder = confReader.globalDownloadDir
            logging.info("couldn't find a series from {}, defaulting to {}".format(file_, downloadFolder))
        logging.info("torrent {0} will be added at path {1}".format(file_, downloadFolder))
        torrent_id = communicator.addTorrent(file_, downloadFolder)

#FIXME
# @main.command()
# def stop():
#     AriaSpawner(getenv("ARIA2C_PATH")).kill()

if __name__ == '__main__':
    main()
    