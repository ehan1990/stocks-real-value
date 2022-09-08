#!/usr/bin/env python
import click
from libs.cmd_api import api_cmd
from libs.cmd_db import db_cmd
from libs.cmd_web import web_cmd
from libs.mongo_service import MongoService
from libs.constants import DB_NAME


@click.group()
def cli():
    pass


cli.add_command(api_cmd)
cli.add_command(db_cmd)
cli.add_command(web_cmd)


if __name__ == "__main__":
    MongoService.init(DB_NAME)
    cli()
