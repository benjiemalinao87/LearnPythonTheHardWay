import lotto
import guessing


def main():
    
    answer = input("Do you want to get lottery numbers (1) or play the game (2) or quit (Q)?")
    if answer == '1':
        numbers = lotto.lotto_numbers()
        print(numbers)
    elif answer == '2':
         guessing.guessing_game_module()
    else : 
        print('Toodles!')
        
main()