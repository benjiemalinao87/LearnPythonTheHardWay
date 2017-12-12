
from sys import argv
from os.path import exists


# script, file_name = argv
script = argv

prompt = '> '

print ('Enter file to be Open & Truncated?[phonebook.txt]:')
filename = input (prompt)
print (f'Does the file exists? {exists(filename)}')


# Opening the file with 'w' argument
print ('Opening the file ...')
target =open(filename, 'a+')



# this hasnt been call yet !!!!
def truncating():
    # Eptying or erasing the content of the file
    print ('Truncating the file. ')
    target.truncate()


# Asking new txt to be writen to the file
print ('Now I am going to ask you for name followed by a mobile number')

name = input('Name: ')
mobile = input ('Mobile: ')

# writing the text to the file
print('Contact successfully added!')
target.write('\n')
target.write(name + ' ' +  mobile)
target.flush()

#  a function reading the file content#
#def read_file(file):

# Display the content of Phonebook.txt to the screen
print ('\n')
print ('-----------------')
print ('    Contacts     ')
print ('-----------------')
with open ('Phonebook.txt','r') as con:
    print (con.read())

# closing file
target.close()

def main():
    pass
