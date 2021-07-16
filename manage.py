import click

from mathfunc.app_main import app


@click.group()
def cli():
    pass


@cli.command()
@click.option('--host', type=str, default='0.0.0.0')
@click.option('--port', type=int, default=5000)
def runserver(host: str, port: int):
    """
    Run Flask dev server
    :param host: host on wich flask will run
    :param port: port where to bind the server
    :return: None
    """
    app.run(host=host, port=port, debug=True)


if __name__ == '__main__':
    cli()
