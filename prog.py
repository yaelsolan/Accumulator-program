import argparse, textwrap

parser = argparse.ArgumentParser(prog='PROG', allow_abbrev=False)
parser.add_argument('--foobar', action='store_true')
parser.add_argument('--foonley', action='store_false')
parser.parse_args(['--foon'])

parser.add_argument('integers', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))

parser = argparse.ArgumentParser(prog='PROG', usage='%(prog)s [options]')
parser.add_argument('--foo', nargs='?', help='foo help')
parser.add_argument('bar', nargs='+', help='bar help')
parser.print_help()
