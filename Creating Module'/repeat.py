import guessing_game

def repeat():
    answer = input ('Do you wish to repeat (Y/N: ')
    
    if answer == 'Y':
        guessing_game.main()
    else :
        print('Goodby! Thanks for using this program!')
    
    
    