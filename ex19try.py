def name():
    print ('Hi how are you?')
    print ('Please enter your name: ')
    namein = str(input())
    return namein
    
def your_name():
    yourname = namein()
    print ('Hi, Welcome {yourname}!')
   
name()
your_name(namein)
    