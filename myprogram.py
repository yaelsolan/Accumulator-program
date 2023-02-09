import argparse
parser = argparse.ArgumentParser(prog='myprogram', description='A foo that bars')
parser.add_argument('--foo', help='foo of the %(prog)s program')
parser.print_help()
