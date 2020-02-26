class CommandFactory(object):
    """ Factory for representing and creating command objects using a generic skeleton. """

    commands = {FsCommand, ...}

    @staticmethod def get_command(argv):
        """ Parse the command line as per the syntax and return command """

        parser = argparse.ArgumentParser(description='EFS CLI command')
        subparsers = parser.add_subparsers()

        for command in CommandFactory.commands:
            command.add_args(subparsers)

        args = parser.parse_args(argv)
        return args.command(args)

class Command(object):
    """ Base class for all commands supported by RAS CLI """

    def __init__(self, args):
        self._args = args

    def action(self):
        return self._args.action

    def args(self):
        return self._args

class FsCommand(Command):
    """ Contains functionality to handle support bundle """

    def __init__(self, args):
        super().__init__(args)

    def name(self): 
        return "fs"

    @staticmethod
    def add_args(parser):
        sbparser = parser.add_parser("fs", help='create, list or delete FS.')
        sbparser.add_argument('action', help='action', choices=['create', 'list', 'delete'])
        sbparser.add_argument('args', nargs='*', default=[], help='fs command options')
        sbparser.set_defaults(command=FsCommand)
