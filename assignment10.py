# Rahul Suthar
# am8633

# imports random module
import random

# makes coin class to create, toss and store value fo the coin
class Coin:
    def __init__(self):
        self.__side_up = random.choice(['heads', 'tails'])
    
    def toss(self):
        self.__side_up = random.choice(['heads', 'tails'])
    
    def get_side_up(self):
        return self.__side_up

# makes game class
class Game:
    # initializes class with player names and choices
    def __init__(self, p1name, p2name, p1choice, p2choice):
        self.__coin = Coin()
        self.__p1name = p1name
        self.__p2name = p2name
        self.__p1choice = p1choice
        self.__p2choice = p2choice

        # sets winner as an empty string
        self.__winner = ""
    
    # tosses coin and has players input their choices and displays winner
    # assumes users wont mess up typing the correct charachters in
    
    def play(self):
        self.__coin.toss()
        self.__p1choice = input(f"{self.__p1name}, pick heads or tails: ").lower()
        self.__p2choice = input(f"{self.__p2name}, pick heads or tails: ").lower()
        print(f"{self.__p1name} tosses the coin...")
        print(f"The coin lands on: {self.__coin.get_side_up()}")
        self.determine_winner()

    
    # determines winner of coin
    # if both players pick same side and coin falls on same side then self.__winner will be set to both players tied
    # if p1.choice = self.__coin.get_side_up() then it will say p1 won
    # if p2.choice = self.__coin.get_side_up() then it will say p2 won
    # if no one guesses correct side then it will put out no one wins
    def determine_winner(self):
        if self.__p1choice == self.__coin.get_side_up() and self.__p2choice == self.__coin.get_side_up():
            self.__winner = "Both players tied!"
        elif self.__p1choice == self.__coin.get_side_up():
            self.__winner = self.__p1name
        elif self.__p2choice == self.__coin.get_side_up():
            self.__winner = self.__p2name
        else:
            self.__winner = "No one. Both of you lost :("
    
    # gets self.__winner
    def get_winner(self):
        return self.__winner

# Looping menu
def main():

    # keepGoing variable controlls loop
    keepGoing = True
    while keepGoing:
        print("\n")
        print("Welcome to Coin Toss!")
        print("-------------------------")
        print("1. Play")
        print("2. Quit")
        choice = input("Enter your choice: ")

        # if choice = 1 then it will play the game
        if choice == '1':
            p1name = input("Enter player 1's name: ")
            p2name = input("Enter player 2's name: ")

            game = Game(p1name, p2name, '', '')
            game.play()
            print(f'The winner is: {game.get_winner()}')

        # if choice = 2 then keepGoing variable becomes false and breaks out of while loop
        elif choice == '2':
            print("Thanks for playing!")
            keepGoing = False
        # if user enters empty string it will ask to enter a valid choice
        elif choice == '':
            print("Please enter a valid choice")
        # if user enters anything else other then 1 or 2 then will ask to enter a 1 or 2
        else:
            print("Invalid choice. Please enter 1 or 2.")

main()
