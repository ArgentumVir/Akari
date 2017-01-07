
def handleArgs():
	import argparse

	parser = argparse.ArgumentParser(description='What measure is a meme?')

	parser.add_argument('--analyze', help='Output whether an image is a meme. [NOT IMPLEMENTED]',
		metavar='file',
		nargs='?',
		type=argparse.FileType('w', encoding='UTF-8')
	)

	parser.add_argument('--create',
		help='Generate a meme. [NOT IMPLEMENTED]',
		metavar=''
	)

	parser.add_argument('--output',
		help='File to store output of Akira. [NOT IMPLEMENTED]',
		metavar='file',
		nargs=1
	)

	parser.add_argument('--training',
		help='File used to train Akira. [NOT IMPLEMENTED]',
		nargs='?',
		metavar='file',
		type=argparse.FileType('w', encoding='UTF-8')
	)

	args = parser.parse_args()
	return;
