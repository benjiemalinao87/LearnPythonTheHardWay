
from sys import argv

# script, file_name = argv
script = argv

prompt = '> '

print ('Enter file to be Open & Truncated?:')
filename = input (prompt)

print (f' We are going to erase {filename}.')
print ('If you odnt want that, hit CTRL-C.')
print ('If you do want that, hit RETURN')

input('?')
# Opening the file with 'w' argument
print ('Opening the file ...')
target = open(filename, 'w')


# Eptying or erasing the content of the file
print ('Truncating the file. Goodbye!')
target.truncate()

# Asking new txt to be writen to the file
print ('Now I am going to ask you for three lines.')
line1 = input('line 1: ')
line2 = input('line 2: ')
line3 = input('line 3: ')


# writing the text to the file
print('I am going to write these to the file.')
target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

# closing file
print ('And finally, we closed it.')
target.close()


