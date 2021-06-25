import subprocess

import click


@click.command()
@click.option('--skip-init/--no-skip-init', default=True,
              help='Skip __init__.py files?')
@click.argument('path', default='sanantonioscientist')
def cli(skip_init, path):
    """Runs flake8 against the code base.

    Parameters
    ----------
    skip_init : bool
        Whether to skip init files for flaking
    path : str, optional
        Test coverage path, by default sanantonioscientist

    Returns
    -------
    int
        Shell exit code
    """
    flake8_flag_exclude = ''

    if skip_init:
        flake8_flag_exclude = ' --exclude __init__.py'

    cmd = f'flake8 {path}{flake8_flag_exclude}'
    return subprocess.call(cmd, shell=True)
