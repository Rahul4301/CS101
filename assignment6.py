# Rahul Suthar
# am8633


def getName():
###########################
    # asks user for name and returns it
    name = input("Enter your name: ")

    # returns the string stored in name
    return name
###########################

def getScore():
###########################
    # asks user for score but there is a failsafe that allows the user to input the score correctly
    try:
        score = float(input("Enter your score: "))
    except ValueError:
        print("ERROR")
        score = float(input("Enter your score: "))

    # returns the value stored in score
    return score
###########################

def newScore():
###########################

    # assigns studentName to getName
    studentName = getName()

    # assigns getScore to score
    score = getScore()

    # opens records.txt in append mode, writes the stident name and score, and closes the file
    records = open('records.txt','a')
    records.write(studentName + '\n')
    records.write(str(score) + '\n')
    records.close()
###########################

def readRecords():
###########################

    # opens records.txt in read mode and returns all the text in the file, closes it and prints it
    records = open('records.txt','r')  
    readRecords = records.read()
    records.close()
    print(readRecords)
###########################    

def getGrade(studentName):
###########################
    # uses try/except as a failsafe if user does not enter a number
    try:
        pointTotal = float(input("Enter the total number of available points: "))
    except ValueError:
        print("ERROR")
        pointTotal = float(input("Enter the total number of available points: "))
    records = open('records.txt','r')

    # sets up a variable for an accumulator with totalScore = 0
    totalScore = 0

    # for all the lines in records it will strip the strings of the new line charachter
    for lines in records:

        name = lines.rstrip('\n')

        # sets condition if name is equal to the studentname
        if name == studentName:

            # returns the lines from reords and strips them of the newline charachter and converts them into floats
            score = records.readline()
            score = score.rstrip('\n')
            score = float(score)

            # accumulator
            totalScore += score
            
        else:
            records.readline()

            
    # divides scores earned by the total points and returns the value
    return totalScore/pointTotal
        
###########################


def menu():
    response = ""
    while response.lower() != "exit":
        print("\n\nWelcome to the grade book")
        print("Choose one of the following: ")
        print("Enter a new test score: <NEW>")
        print("Read all scores: <READ>")
        print("Get Student grade: <GRADE>")
        print("Exit the program: <EXIT>")
        response = input(" :: ")
        if response.lower() == "read":
            readRecords()
        elif response.lower() == "new":
            newScore()
        elif response.lower() == "grade":
            name = input("Enter the student name: ")
            score = getGrade(name)
            print(name + " overall score is " + str(score))
        elif response.lower() != "exit":
            print("Invalid response")

def main():
    menu()
    print("Thank you for using the gradebook")

main()
