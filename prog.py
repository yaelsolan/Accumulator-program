import argparse

parser = argparse.ArgumentParser(
	prog='PROG',
	description='''this description
	was indented weird
	but that is okay''',
	epilog='''
		likewise for this epilog whose whitespace will
	be cleand up and whose words will be wrapped
	across a couple lines''')
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
