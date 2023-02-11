import argparse

parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('-f', '--foo', help='old foo help')
parser.add_argument('--foo', help='new foo help')

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
