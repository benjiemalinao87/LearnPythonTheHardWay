from sys import argv
try: 
    script, first, second, third = argv 

    print ('The script is called: ', script)
    print('The first variable is : ', first)
    print ('The second variable is : ', second)
    print ('The third variable is :: ', third)
except ValueError as err:
    print(err)