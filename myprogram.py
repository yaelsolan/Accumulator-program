import argparse
parser = argparse.ArgumentParser(prog='myprogram')
parser.add_argument('--foo', help='foo of the %(prog)s program')
parser.print_help()
