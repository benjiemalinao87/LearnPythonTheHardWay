from sys import argv

script = argv

print (f'Enter filename of the file you want to open: ')
filename = input()
txt = open(filename)

print (f'Here is your file {filename}: ')
print (txt.read())

try: 
    print ('type the filename again: ')
    text_again = input('> ')

    text_again = open (text_again)

    print (text_again.read())
except FileNotFoundError as err:
    print (err)

