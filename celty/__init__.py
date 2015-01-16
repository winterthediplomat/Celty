from __future__ import print_function, unicode_literals
import argparse

parser = argparse.ArgumentParser(
	description="""Celty: combine Miyuki and aria2c for the ultimate anime downloader!""",
	epilog="remember to add 'aria2c' to your path!")
parser.add_argument("miyuki_path", help="the path to the Miyuki configuration file")

def main():
    """Where the journey begins..."""
    args = parser.parse_args()
    print(args.miyuki_path)