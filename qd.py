import quopri
import argparse
import codecs
parser = argparse.ArgumentParser(description='give me some files')

parser.add_argument("input", help="Quoted Printable input file")
parser.add_argument("output", help="Decoded output file")

args = parser.parse_args()

in_file = open(args.input, mode='r')
quoted_text = in_file.read()
in_file.close()

decoded = quopri.decodestring(quoted_text)
decoded = decoded.replace('\r\n', '\n');
decoded = decoded.decode('utf-8', 'replace')

out_file = codecs.open(args.output, encoding='utf-8', mode='w+')
out_file.write(decoded)
out_file.close()
