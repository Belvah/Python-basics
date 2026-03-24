word='banana'
#traversal/visiting each character in the string
index =0 #initialization

while index < len (word): #condition/while loop
    char = word[index] #variable to store chracter.x is the variable and can be anything.
print (f'index{index} contains: {char}')
index +=1 #incrementing the index to move to the next character

    #For loop to traverse the string without using the index
for char in word:
         print(char)

#comment out while loop. Using for loop to count how many times 'a' appears in the word 'banana'
for char in word:
            if char == 'a':  #how many times a appears
                index=index+1
                print(index)

    #CHECK IF CHAR EXISTS IN THE STRING
    
for char in word:
        if char == 'n':
            index== index +1
            print(index)
            print('en' in word)#returns boolean

#Another example of checking if a character exists in the string
email="kwanusu@gmail.com"
print('gmail' in email) #returns boolean

fruit ='Pineapple'
if fruit <'banana' :
       print('Pineapple comes first')