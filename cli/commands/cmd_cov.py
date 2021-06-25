import subprocess

import click


@click.command()
@click.argument('path', default='sanantonioscientist')
def cli(path):
    """Run a test coverage report in the shell.

    Parameters
    ----------
    path : path, optional
        Test coverage path, by default sanantonioscientist

    Returns
    -------
    int
        Shell exit code
    """
    cmd = 'python -m pytest sanantonioscientist --cov-report html:cov ' + \
        f'--cov {path}'
    return subprocess.call(cmd, shell=True)
