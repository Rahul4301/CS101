# Rahul Suthar am8633
print('Trip PLanner')

#prompts user to input number of miles they will drive
numMile = float(input("How many miles will you drive? "))

#prompts user to input how fast they will drive
numVel = float(input('How fast do you drive? '))

#prompts user to input how many stops they will take
numStop = float(input('How many stops will you make? '))

#prompts user to input how long each stop will be
stopTime = float(input('How long is each stop? (in minutes): '))

#timeTotal calculates how long the trip will take in hours
hourTotal = (numMile/numVel) + (numStop*stopTime/60)

#minTotal calculates how long the trip will take in minutes
minTotal = hourTotal*60

#prints out the output of the equations into the string
print('Your trip will take ', str(minTotal), " minutes, or",str(hourTotal),'hours')
