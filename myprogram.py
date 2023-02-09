import argparse
parser = argparse.ArgumentParser(
	prog='myprogram',
	description='A foo that bars',
	epilog="And that's how you'd foo a bar")
parser.add_argument('--foo', help='foo of the %(prog)s program')
parser.print_help()
