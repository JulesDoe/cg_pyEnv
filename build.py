import os
import sys

if (len(sys.argv) < 2):
	print("Error, expected which file to build", file=sys.stderr)
	exit()

output_file = "cg.out"
input_file = sys.argv[1]

def parse_import(line):
	f_loc = ""
	line_args = line.strip().split()
	for i, w in enumerate(line_args):
		if (w == 'from'):
			f_loc = line_args[i+1]
			break
	f_loc = [t for t in f_loc.split('.') if len(t) > 0]
	f_loc = '/'.join(f_loc) + '.py'
	print(f_loc, file=sys.stderr)
	return f_loc

def flush_imports(ostream, impt_files):
	print(f"Importing files: {impt_files}", file=sys.stderr)
	for f in impt_files:
		is_importing = False
		with open(f,'r') as fin:
			for line in fin:
				line_args = line.split()
				# Ignore imports in subfiles
				if (len(line_args) > 0 and (line_args[0] == 'from' or line_args[0] == 'import')):
					pass
				elif line.strip() == "#IMPORT":
					# Start import
					is_importing = True
				elif line.strip() == "#ENDIMPORT":
					# Stop import
					is_importing = False
				else:
					ostream.write(line)
		ostream.write("\n\n")

is_importing = False
imported_files = []
with open(output_file, 'w+') as fout:
	with open(input_file, 'r') as fin:
		for line in fin:
			if line.strip() == "#IMPORT":
				# Start import
				is_importing = True
			elif line.strip() == "#ENDIMPORT":
				# Stop import
				is_importing = False
				flush_imports(fout, imported_files)
			elif (is_importing):
				line_args = line.split()
				if (len(line_args) > 0 and (line_args[0] == 'from' or line_args[0] == 'import')):
					imported_files.append(parse_import(line))
			else:
				fout.write(line)