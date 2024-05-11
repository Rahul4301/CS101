# Rahul Suthar
# am8633

print('Welcome to Rock, Paper, Scissors')


import random
def rpsChoice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

#prompts user of they are playing with a friend or with the computer
friendOrcomputer = input("Are you playing with a friend(F) or against the computer(C)? Enter F or C: ").upper()


#if statement for if the user wants to play with the computer
if friendOrcomputer == 'C':

    #assigns rpsChoice to computer
    computerChoice = rpsChoice()

    #prompts user for their name
    userName = input('What is your name?: ')


    #next line
    print('\n')

    #prompts user to pick rock paper scissors
    userOption = input(f'{userName}, pick Rock, Paper, Scissors: ').lower()
    print('\n')

    #if statement if there were a tie
    if userOption == computerChoice:
        print('\n')
        print(f"You and the computer both picked {userOption}. You tied!")

    #elif statement if the user picked rock and the computer picked scissors    
    elif userOption == 'rock' and computerChoice == 'scissors':
        print(f'{userName} picked {userOption}')
        print(f'The computer picked {computerChoice}.')
        print('\n')
        print(f'{userName} wins!')

    #elif statement if the user picked scissors and the cumputer picked paper
    elif userOption == 'scissors' and computerChoice == 'paper':
        print(f'{userName} picked {userOption}')
        print(f'The computer picked {computerChoice}.')
        print('\n')
        print(f'{userName} wins!')

    #elif statement if the user picked paper and the computer picked rock
    elif userOption == 'paper' and computerChoice == 'rock':
        print(f'{userName} picked {userOption}')
        print(f'The computer picked {computerChoice}.')
        print('\n')
        print(f'{userName} wins!')

    #else statement if the computer picked something that did not correspond with the conditions in the elif statements
    else:
        print(f'{userName} picked {userOption}')
        print(f'The computer picked {computerChoice}.')
        print('\n')
        print('The computer wins!')

#elif statement if user picks F
elif friendOrcomputer == 'F':
    print('\n')

    #promtps and assigns the names of the players to the variables p1 and p2
    p1 = input("Player 1 please enter your name: ")
    p2 = input('Player 2 please enter your name: ')
    print('\n')

    #promtps the players to pick rock paper scisors and assigns them in p1choice and p2choice
    p1choice = input(f'{p1}, please choose rock, paper, or scissors: ').lower()
    p2choice = input(f'{p2}, please choose rock, paper, or scissors: ').lower()

    #if statement if both players tied
    if p1choice == p2choice:
        print('\n')
        print(f'{p1} and {p2} both picked {p1choice}. You both tied!')

    #elif statement if p1 picked rock and p2 picked scissors
    elif p1choice == 'rock' and p2choice =='scissors':
        print('\n')
        print(f'{p1} picked {p1choice}')
        print(f'{p2} picked {p2choice}.')
        print('\n')
        print(f'{p1} wins!')

    #elif statement if p1 picked scissors and p2 picked paper
    elif p1choice == 'scissors' and p2choice =='paper':
        print('\n')
        print(f'{p1} picked {p1choice}')
        print(f'{p2} picked {p2choice}.')
        print('\n')
        print(f'{p1} wins!')
        
    #elif statement if p1 picked paper and p2 picked rock
    elif p1choice == 'paper' and p2choice =='rock':
        print('\n')
        print(f'{p1} picked {p1choice}')
        print(f'{p2} picked {p2choice}.')
        print('\n')
        print(f'{p1} wins!')

    #else statement if p2 picked something that did not correspond with the conditions of the elif statements above
    else:
        print('\n')
        print(f'{p1} picked {p1choice}')
        print(f'{p2} picked {p2choice}.')
        print('\n')
        print(f'{p2} wins!')

#else statement if the user did not pick f or c
else:
    print('\n')
    print('Please pick either F or C')
