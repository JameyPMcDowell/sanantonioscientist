import os
import subprocess

import click


@click.command()
@click.argument('path', default=os.path.join('sanantonioscientist', 'tests'))
def cli(path):
    """Run tests with Pytest

    Parameters
    ----------
    path : str, optional
        Test path, by default sanantonioscientist/tests

    Returns
    -------
    int
        Shell exit code
    """
    cmd = f'py.test {path}'
    return subprocess.call(cmd, shell=True)
