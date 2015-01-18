from __future__ import print_function, unicode_literals
import click
from .conf import ConfReader
from .communicator import AriaCommunicator, AriaSpawner
from .fs import TorrentFinder
import logging
from os.path import expandvars
from os import getenv
logging.basicConfig(filename=expandvars("$HOME/.celty.log"))

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
    # if not communicator.isRunning():
    #     spawner = AriaSpawner(getenv("ARIA2C_PATH"))
    #     spawner.spawn(confReader.aria2Port, confReader.aria2UseSecret, confReader.aria2FixedRPCSecret)
    torrentFinder = TorrentFinder(confReader.watchDir)
    for file_ in torrentFinder.list():
        torrent_id = communicator.addTorrent(file_, confReader.globalDownloadDir) #TODO: each show in its own folder!
        logging.info("torrent {0} has been added, its id is {1}".format(file_, torrent_id))

@main.command()
def stop():
    AriaSpawner(getenv("ARIA2C_PATH")).kill()

if __name__ == '__main__':
    main()
    