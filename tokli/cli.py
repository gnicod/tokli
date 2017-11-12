import click
import json
import sys
from tokli.config import Config
from tokli.api import Api
from tokli.exceptions import ConfigNameUnknown


@click.group()
def cli_list():
    pass


@cli_list.command()
def list():
    """List all configured apis"""
    print(json.dumps(Config.get_apis()['apis'], indent=4, sort_keys=True))


@click.group()
def cli_get():
    pass


@cli_get.command()
@click.argument('name')
@click.option('--refresh', is_flag=True)
def get(name, refresh):
    """retrieve a token """
    try:
        api = Api(
            **Config.get_config_api(name),
            name=name,
            force_refresh=refresh)
    except ConfigNameUnknown:
        print('Config name %s does not exist' % name)
        sys.exit(2)
    token = api.get_token()
    print(token)


cli = click.CommandCollection(sources=[cli_list, cli_get])

if __name__ == '__main__':
    cli()
