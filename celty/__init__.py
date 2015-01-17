from __future__ import print_function, unicode_literals
import click

@click.group()
def main():
    """Where the journey begins..."""
    pass

@main.command()
@click.argument("miyuki-path")
def start(miyuki_path):
    raise NotImplementedError("start {0}".format(miyuki_path))

@main.command()
def stop():
	raise NotImplementedError("stop")

if __name__ == '__main__':
	main()
    