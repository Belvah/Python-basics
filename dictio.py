alphabets = dict() #or initialize with e.g my_dict = {}
alphabets['a'] = 'apple'
alphabets['b'] = 'ball'
alphabets['c'] = 'cat'
my_dict = {}
#my_dict = {'a': 'apple', 'b': 'ball', 'c': 'cat'} Gives same output/another initialization method
print(alphabets) #prints key and value pairs i.e a : apple, b : ball, c : cat

print(alphabets['a']) #prints value of key a i.e apple

#print length of dictionary
print(len(alphabets)) #prints 3 as there are 3 key value pairs

#TO CHECK IF A KEY EXISTS IN THE DICTIONARY-in function.
#e.g to check if key 'a' exists in the dictionary
print('a' in alphabets)  #prints True as key a exists in the dictionary
print(alphabets.keys()) #prints/check all the keys in the dictionary
print(alphabets.values()) #prints/check all the values in the dictionary
print('cat' in alphabets) #does not loop values.)

#declare a variable(fname)
fname = input("Enter a file name \n")
fhand = open(fname) #open the file and assign it to a variable(fhand)

#count how many kids we have example.
count = dict()
for line in fhand: #loop through each line in the file
    words = line.split() #split the line into words and assign it to a variable(words)
    for word in words: #loop through each word in the line
        count[word] = count.get(word, 0) + 1 #get the count of the word and add 1 to it. If the word does not exist, get returns 0 and adds 1 to it.

print(count) #prints the count of each word in the file.

#DATA CLEANING

import string
fname = input("Enter a file name \n")

#ERROR HANDLING
try: #to handle the error if the file does not exist 
    fhand = open(fname) #open the file and assign it to a variable(fhand)
except: #if the file does not exist, print an error message and exit the program 
    print("File cannot be opened:", fname)

    exit()

count = dict()

for line in fhand: #loop through each line in the file

    words = line.rstrip() #to remove spaces from right side of the line

    table = str.maketrans ('' , '' , string.punctuation) #to remove punctuation from the line(table is variable with cleaned words)

    words = line.translate(table)

    words = words.lower() #to convert all words to lower case

    words= line.split() #split the line into words and assign it to a variable(words)

    for word in words: #loop through each word in the line
        
        count[word] = count.get(word, 0) + 1 #get the count of the word and add 1 to it. If the word does not exist, get returns 0 and adds 1 to it.

print(count) #prints the count of each word in the file.
