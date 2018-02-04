phonebooks = {}

prompt = '>'

print('-------------------')
print(' Phonebooks System  ')
print('-------------------')
print('\n')

target = open('phonebooks.txt', 'a+')

def load_phonebook():
    for line in target:
        keys = line.split()
        phonebooks[keys[0]] = keys[2]
        print(keys)
    return phonebooks

def dump_phonebook():
    target = open('phonebooks.txt', 'w+')
    # print('Writing to file.... ')
    for name in phonebooks:
        target.write(name  + " = " + phonebooks[name] + "\n")
        #print('Writing ' + name + " to the file")
    target.close()

def name_mobile():
    print('\n')
    print ('Enter name and mobile to add to phonebooks')
    add_name = str(input('Enter name: '))
    add_mobile = str(input('Enter mobile number: '))
    phonebooks[add_name] = add_mobile
    print(phonebooks)
    return phonebooks

def addname_mobile():
    #print('Writing on the file...please wait...SUCCESSFULL ADDED!')

    target = open('phonebooks.txt', 'a+')
    for key, val in phonebooks.items():
        target.write(key + ' = ' + val + '\n')
        return target
    target.close()


def delete_contact():
    #target = open('phonebooks.txt')
    delete_record = input('Please enter name to delete record: ')
    print(phonebooks)
    for record in list(phonebooks.keys()):
        if record == delete_record:
            del phonebooks[record]
    
            print('Contact deleted!')
    return phonebooks
   

    #target.close()

def clear_record():
    target = open('phonebooks.txt', 'w+')
    for key, val in phonebooks.items():
        phonebooks.clear()
    print('Record has benn deleted!')
    target.close()


def choice():
    print(phonebooks)
    print('Choose Operation, 1 - Add, 2- delete, 3 - delete-all, a record')
    ans = input(prompt)
    if ans == '1':
        name_mobile()
        addname_mobile()
    elif ans == '2':
        
        delete_contact()
        #print(phonebooks)

    elif ans == '3':
        clear_record()
    else:
        print('Invalid input!')
     

target = open('phonebooks.txt','r')
#phonebooks.items()
#print(target.read())

load_phonebook()
#print(phonebooks)


target.close()

choice()
dump_phonebook()

#name_mobile()
#addname_mobile()


    






