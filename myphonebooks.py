phonebooks = {}

prompt = '>'

print('-------------------')
print(' Phonebooks System  ')
print('-------------------')
print('\n')


def name_mobile():
    print('\n')
    print ('Enter name and mobile to add to phonebooks')
    add_name = str(input('Enter name: '))
    add_mobile = str(input('Enter mobile number: '))
    phonebooks[add_name] = add_mobile

    print(phonebooks)

    print('Writing on the file...please wait...SUCCESSFULL ADDED!')
  # target.write(phonebooks[add_name] + [add_mobile])

    target = open('phonebooks.txt', 'a+')
    for key, val in phonebooks.items():
        target.write(key + ' = ' + val + '\n')
   
  

    

name_mobile()


    






