from sys import argv
from os.path import exists

script = argv


print("Enter source file to be copied: ")
from_file = input()
print("Enter destination file: ")
to_file = input()

# Copying from_file to to_file (source file to destinaton file)
print (f"Copying from {from_file} to {to_file}")
# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

# --------------
# Getting the size of the file using len function
print (f"The input file is {len(indata)} bytes long")

# Comparing id the file exists using imported exists module
print (f"Does the output file exist? {exists(to_file)}")
print ("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

# Open & ready to write to_file from indata(infile/from_file). See above conatainer passing
out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

# CLosing the two files
out_file.close()
in_file.close()