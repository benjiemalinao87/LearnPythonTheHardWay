phonebooks = {}

prompt = '>'

print('-------------------')
print(' Phonebooks System  ')
print('-------------------')
print('\n')

target = open('phonebooks.txt', 'a+')

def name_mobile():
    print('\n')
    print ('Enter name and mobile to add to phonebooks')
    add_name = str(input('Enter name: '))
    add_mobile = str(input('Enter mobile number: '))
    phonebooks[add_name] = add_mobile
    print(phonebooks)
    return phonebooks
    target.close()

def addname_mobile():
    print('Writing on the file...please wait...SUCCESSFULL ADDED!')

    target = open('phonebooks.txt', 'a+')
    for key, val in phonebooks.items():
        target.write(key + ' = ' + val + '\n')
        return target
    target.close()




        
def delete_contact():
    
    print('Please enter name to delete record: ')
    delete = input(prompt)
    for key in phonebooks.items():
        del phonebooks[delete]
    print('Successully deleted!')
    return target
    return phonebooks
    target.close()

def clear_record():

    for key, val in phonebooks.items():
        phonebooks.clear()
    print('Record has benn deleted!')
    target.close()


def choice():
    print('Choose Operation, 1 - Add, 2- delete, 3 - delete-all, a record')
    ans = input(prompt)
    if ans == '1':
        name_mobile()
        addname_mobile()
    elif ans == '2':
        delete_contact()
    elif ans == '3':
        clear_record()
    else:
        print('Invalid input!')
     

target = open('phonebooks.txt')   
phonebooks.items()
print(target.read())

print('DO you want to delete the record before proceeding: ')
ans = input()
if ans == 'Y':
    phonebooks.clear()
    print('Successfully deleted')
else:
    pass

choice()

#name_mobile()
#addname_mobile()


    






