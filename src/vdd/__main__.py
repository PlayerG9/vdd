# -*- coding=utf-8 -*-
r"""

"""
import argparse as ap
import vdd
try:
    import better_exceptions
    better_exceptions.hook()
except ModuleNotFoundError:
    pass


parser = ap.ArgumentParser("vdd", description=__doc__, formatter_class=ap.ArgumentDefaultsHelpFormatter)
parser.set_defaults(fn=parser.print_help)
subparsers = parser.add_subparsers()

init_parser = subparsers.add_parser("init",
                                    help="Initialize the database")
init_parser.set_defaults(fn=vdd.database.__cmd__)


add_parser = subparsers.add_parser("add",
                                   help="Add a video to the database")
add_parser.set_defaults(fn=vdd.adding.__cmd__)


find_parser = subparsers.add_parser("find",
                                    help="Find duplicates in the database")
find_parser.set_defaults(fn=vdd.finding.__cmd__)


def main():
    arguments = vars(parser.parse_args())
    fn = arguments.pop('fn')
    fn(**arguments)


if __name__ == '__main__':
    main()
