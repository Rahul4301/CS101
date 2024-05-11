# Rahul Suthar
# am8633

# function to read words from a file and convert them to Pig Latin
def piglatin(sentence):

    # list of vowels
    vowels = ['a','e','i','o','u','A','E','I','O','U']

    # splits sentence argument into words
    words = sentence.split()

    # stores translated pig latin sentence
    pigsentence = ""

    # for loop that will go through each work in the sentence
    for word in words:
        accum = 0
        a = False
        for letter in word:
            # checks if letter is a vowel and if it's the first vowel in word
            if letter in vowels and a == False:

                # shows that vowel was found and translates into pig latin
                a = True
                pigword = word[accum:] + word[:accum] + "ay"
                pigsentence += pigword + " "
              
            else:
                # keeps track of positions in the word as it loops through
                accum += 1
                
        # if word has no vowels it adds ay
        if a == False:
            pigsentence += word + "ay "
            
    return pigsentence



def wordsfile():
    try:
        # opens words.txt file and reads lines and stores into englishwords
        words = open('words.txt','r')
        englishwords = words.readlines()
        
        # opens file to write and calls piglatin funciton to translate and write to file 
        wordsoutfile = open('piglatin.txt', 'w')
        for line in englishwords:
            line = line.strip()
            wordsoutfile.write(piglatin(line) + '\n')
        print("Conversion completed successfully!")

        # closes files
        words.close()
        wordsoutfile.close()

    # prints file not found if FileNotFoundError
    except FileNotFoundError:
        print("File not found")

# calls wordsfile
wordsfile()
