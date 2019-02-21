# -*- coding: utf-8 -*-

"""Console script for eazyserver."""
import sys
import click

@click.group()
def cli():
    """Console script for eazyserver."""
    click.echo("Replace this message by putting your code into "
               "eazyserver.cli.cli")
    click.echo("See click documentation at http://click.pocoo.org/")

@cli.command()
def run():
    click.echo('Run subcommand')

@cli.command()
def start():
    click.echo('Start subcommand')


if __name__ == "__main__":
    sys.exit(cli())  # pragma: no cover
