import os

import click

cmd_folder = os.path.join(os.path.dirname(__file__), 'commands')
cmd_prefix = 'cmd_'


class CLI(click.MultiCommand):
    def list_commands(self, ctx):
        """Obtain a list of all available commands.

        Parameters
        ----------
        ctx : click.core.Context
            Internal object, that holds state relevant for the script execution
            at every single level.  Used to pass internal objects around and
            control special execution features such as reading data from
            environment variables.

        Returns
        -------
        list
            List of sorted commands
        """
        commands = []

        for f in os.listdir(cmd_folder):
            if f.endswith('.py') and f.startswith(cmd_prefix):
                # ignores cmd_ and .py at end of cmd
                commands.append(f[4:-3])

        commands.sort()

        return commands

    def get_command(self, ctx, name):
        """[summary]

        Parameters
        ----------
        ctx : click.core.Context
            Internal object, that holds state relevant for the script execution
            at every single level.  Used to pass internal objects around and
            control special execution features such as reading data from
            environment variables.
        name : str
            Name of command

        Returns
        -------
        click.core.Command
            Contains methods such as 'get_help', around the command name.
        """
        ns = {}

        filename = os.path.join(cmd_folder, cmd_prefix + name + '.py')

        with open(filename) as f:
            code = compile(f.read(), filename, 'exec')
            eval(code, ns, ns)

        return ns['cli']


@click.command(cls=CLI)
def cli():
    """ Commands to help manage the project. """
    pass
