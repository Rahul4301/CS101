## Rahul Suthar
## am8633

## get random choice function
## Takes no arguments
## Returns one of three strings randomly
## To add more choices, add more strings to choices
import random
def getRandomChoice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

## get choice from user function
## Input validation
## Takes no arguments
## Takes user input and validates against choices
## Returns ONLY one of choice strings
## To add more choices, add more strings to choices
def getChoice():
    choices = ['rock', 'paper', 'scissors']
    userChoice = ""
    while userChoice not in choices:
        userChoice = input("Choice rock, paper, or scissors: ")
    return userChoice.lower()

## get mode function
## Input validation
## Takes no arguments
## Takes user input and validates against choices
## Returns ONLY one of choice strings
## Continue to prompt for choice until user enters a valid answer
## To add more choices, add more strings to choices
def getMode():
    choices = ['friend', 'computer', 'auto']
    ##################
    while True:
        #asks user to pick a mode from choices and stores it in mode
        mode = input('Would you like to play against a computer, friend or auto: ').lower()

        #if mode is in choices then it will call on the play function
        if mode in choices:
            play(mode)
            return mode
        #if user choice is not in choices then it will print invalid input and the loop will start again
        else:
            print("Invalid input. Please enter a valid mode.")
    ##################


## get number function
## Input validation
## Error handling
## returns an int between 0 and max number'
## Will not return an unsafe number
## Will not return negative or greater than max number
## Bad user input returns 0
def getNum(max):
    userNumber = input("Enter a number from 0 to " + str(max) + ": ")
    try:
        max = int(max)
        userInt = int (userNumber)
        if userInt > max:
            return max
        elif userInt < 0:
            return 0
        else:
            return userInt

    except ValueError:
        print("Invalid input. Returning zero")
        return 0

## get name function
## Input validation
## takes no arguments
## returns user input string
## Must not allow for a blank name
def getName():
    ##################
    while True:

        #asks user for their name and stores it in userName
        userName = input("Enter your name: ")

        #if userName is not equal to an empty string then it will return userName
        if userName != "":
            return userName

        #if userName is equal to an empty string it will print invalid input and the loop will start again
        else:
            print("Invalid input. Please enter a non-empty name.")
    ##################

## get winner function
## Pass in player choices and player names as string arguments
## This function will decide the winner and give output
## Output includes displaying the players names and choices
def getWinner(p1Choice, p2Choice, p1Name, p2Name):
    ##################
    #promtps and assigns the names of the players to the variables p1 and p2
    if p1Choice == p2Choice:
        print('\n')
        print(f'{p1Name} and {p2Name} both picked {p1Choice}. You both tied!')
        print('\n')

    #elif statement if p1 picked rock and p2 picked scissors or if p1 picked scissors and p2 picked paper or if p1 picked paper and p2 picked rock
    elif (p1Choice == 'rock' and p2Choice =='scissors') or (p1Choice == 'scissors' and p2Choice =='paper') or (p1Choice == 'paper' and p2Choice =='rock'):
        print('\n')
        print(f'{p1Name} picked {p1Choice}')
        print(f'{p2Name} picked {p2Choice}.')
        print('\n')
        print(f'{p1Name} wins!')
        print('\n')


    #else statement if p2 picked something that did not correspond with the conditions of the elif statement above
    else:
        print('\n')
        print(f'{p1Name} picked {p1Choice}')
        print(f'{p2Name} picked {p2Choice}.')
        print('\n')
        print(f'{p2Name} wins!')
        print('\n')
    ##################

## Main function 
## Prints a banner
## Calls the menu function
def main():
    print("Welcome to the Rock Paper Scissors game Version 1.01")
    menu()
    print("End of Main")

## Menu Function
## Loops on the again flag
## Validates input on prompt
## Case insensitive
## Calls play function on "yes" or "y"
## Breaks loop on "no" or "n"
## Output "invalid input" on anything else
def menu():
    ##################
    #calls getMode
    mode = getMode()

    keepGoing = 'yes'
    while keepGoing.lower() == 'yes' or keepGoing.lower() == 'y':

        

        #calls play function
        play(mode)

        print('\n')

        keepGoing = input("Would you like to keep going? Enter 'yes' or 'y' to continue. If not, enter 'no' or 'n' to exit: ")
    
    
    ##################

# Play function
def play(mode):
    if mode.lower() == "computer":
        p1Name = "Computer"
        p2Name = getName()
        p1Choice = getRandomChoice()
        p2Choice = getChoice()
    elif mode.lower() == "friend":
        p1Name = getName()
        p2Name = getName()
        p1Choice = getChoice()
        p2Choice = getChoice()
    elif mode.lower() == "auto":
        p1Name = "Auto P1"
        p2Name = "Auto P2"
        p1Choice = getRandomChoice()
        p2Choice = getRandomChoice()
    else:
        print("Error")
        return

    getWinner(p1Choice,p2Choice,p1Name,p2Name)
    print("Thank you for playing")

# Call main function
main()
