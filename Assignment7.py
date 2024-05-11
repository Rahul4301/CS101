# Rahul Suthar
# am8633

#promtps user for a number greater than 1. if number is not greater than 1, will prompt to enter again
def intUserPrompt():
    try:
        num = int(input('Please enter a number greater than 1: '))

    except ValueError:
        print("ERROR: you did not input a number larger than 1")
        num = int(input('Please enter a number greater than 1: '))

    #returns num
    return num

n = intUserPrompt()

### START OF PROVIDED CODE ###
def prime_or_composite(n):
    has_divisor = False
    for i in range(2, n):
        if n % i == 0:
            has_divisor = True
    if has_divisor:
        return False
    else:
        return True

### END OF PROVIDED CODE ###

    
def primeCompositeList():
    # creates empty lists
    primes = []
    composites = []

    # creates for loop that runs prime_or_composite(n) for n amount of times and appends accordingly
    for x in range(1, n+1):
        if prime_or_composite(x):
            primes.append(x)
        else:
            composites.append(x)
    return primes, composites

results = primeCompositeList()

# creates file writing variable in which the lists will print
def listOutfile(n, filename):
    n = str(n)

    #removes brackets
    n = n[1:len(n)-1]
    listFile = open(filename, 'w')
    listFile.write(n + '\n')
    listFile.close()


# calls listOutFile function and prints the lists to the respective files
listOutfile(results[0], 'primes.txt')
listOutfile(results[1], 'composites.txt')
