from os.path import exists

from_file = raw_input("Enter From file path: ")
to_file = raw_input("Enter To file path: ")

indata = open(from_file).read()

print "The input file is %d bytes long" %len(indata)

print "Does the output file exists? %s" %exists(to_file)

open(to_file,'w').write(indata)
