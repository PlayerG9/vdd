# -*- coding=utf-8 -*-
r"""

"""
import argparse as ap
try:
    import better_exceptions
    better_exceptions.hook()
except ModuleNotFoundError:
    pass


parser = ap.ArgumentParser("vdd", description=__doc__, formatter_class=ap.ArgumentDefaultsHelpFormatter)
parser.set_defaults(fn=parser.print_help)


def main():
    arguments = vars(parser.parse_args())
    fn = arguments.pop('fn')
    fn(**arguments)


if __name__ == '__main__':
    main()
