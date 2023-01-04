import random

print ('WELCOME TO GUESS GAME')

print ('I am thinking of a number between 1 and 100')


def game() :

    answer = random.randint(1, 100)


    turns = game_level()

    guess = 0 
    
    while guess != answer :
        
        print(f'You have {turns} attemps remaining to guess th number ')

        guess = int(input('Make a guess  : '))
    
        turns = check_answer(guess, answer, turns)

        if turns == 0 :
            print("You have run out of guesses, you lose")

            return
        elif guess != answer :
            print('Guess again')


def check_answer(guess, answer, turns) :
    if guess > answer :
        print('Too high')
        return turns -1 

    elif guess < answer :
        print ('Too low') 
        return turns -1 
    else :
        print(f'You got it {answer}')

easy_Level = 10

hard_Level = 5

def game_level() :

    level_chose = input("Choose difficulty 'Easy' or 'Hard' ")

    if level_chose == "easy" :

     return easy_Level

    elif  level_chose == "hard" :

        return hard_Level



game()

