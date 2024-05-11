# Rahul Suthar
# am8633


# function to find the word
def search_word(word):
    if word in wordIndex:
        print(f"The word '{word}' appears {wordIndex[word]} times in the file.")
    else:
        print(f"The word '{word}' is not found in the file.")


def most_frequent_word():
    max_frequency = 0
    most_frequent_word = ""

    # for loop to look over eah work in word index dictionary
    for word in wordIndex:
        # gets frequency of current word and checks if frequency is greater than the maximum
        frequency = wordIndex[word]
        # if greater than maximum then it updates maximum frequency and most frequent word
        if frequency > max_frequency:
            max_frequency = frequency
            most_frequent_word = word

    if most_frequent_word:
        print("The word that appears most frequently is '" + most_frequent_word + "' with " + str(max_frequency) + " occurrences.")
    else:
        print("No words found in the file.")

def least_frequent_word():
    
    min_frequency = 0
    least_frequent_word = ""

    # for loop to look over eah work in word index dictionary
    for word in wordIndex:
        # gets frequency of current word and checks if frequency is less than the minimum
        frequency = wordIndex[word]
        # if less than the minimum then it updates minimum rrequency and least frequent word
        if frequency < min_frequency or min_frequency ==0:
            min_frequency = frequency
            least_frequent_word = word

    if least_frequent_word:
        print("The word that appears least frequently is '" + least_frequent_word + "' with " + str(min_frequency) + " occurrence(s).")
    else:
        print("No words found in the file.")

def menu():
    print("\nMenu:")
    print("#1 - Find a word in the dictionary")
    print("#2 - Find the most requently seen word")
    print("#3 - Find the least frequently seen word")
    print("#4 - Exit")


# loops until it finds a file
fileFound = False
while fileFound == False:
    try:
        filename = input("Enter filename for the input: ")
        infile = open(filename, "r")
        fileFound = True
    except FileNotFoundError:
        print("File not found. Please try again.")

wordIndex = {}

### START OF PROVIDED CODE
lines = infile.readlines()

for line in lines:
    line = line.rstrip('\n')
    words = line.split()
    for word in words:
        if word in wordIndex:
            wordIndex[word] += 1
        else:
            wordIndex[word] = 1

print(wordIndex)
### END OF PROVIDED CODE


# looping menu
# allows people to decide if they want to look for a word, find most frequent, least frequent word, or exit
project = True
while project:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        word_to_search = input("Enter the word to search for: ")
        search_word(word_to_search)
    elif choice == "2":
        most_frequent_word()
    elif choice == "3":
        least_frequent_word()
    elif choice == "4":
        print("Exiting program...")
        project = False
    else:
        print("Invalid choice")
