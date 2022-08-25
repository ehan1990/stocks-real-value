#!/usr/bin/env python
import click
from libs.cmd_stock import stock_cmd
from libs.mongo_service import MongoService


@click.group()
def cli():
    pass


cli.add_command(stock_cmd)


if __name__ == "__main__":
    MongoService.init("tothemoon")
    cli()
