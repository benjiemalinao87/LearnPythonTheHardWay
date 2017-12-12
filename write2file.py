from sys import argv

script = argv


def create_a_file():
    #creating a file from user input
    print ('Enter a filename of the file you want to create: ')
    file = str(input())
    texts = open(file, 'w')
    print ('creating a file . . . . . File created successfully! ')
    

    #writing txt to a existing file
    texts.write('Text is hardcolly added')
    print (f'Here is your final file, {file} ')
        
    #Deleting the text on the file 
    print(input())
    print ('Truncating the file...')
    texts.truncate()
    
    print ('Now I am going to ask one line of txt')
    line1 = input('this is a line 1:')
    
    print('I am going to write this line to the file.')
    
    texts.write(line1)
    
    texts.close()
            
create_a_file() 



