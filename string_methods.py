my_string= "python Programming"
#print(len(my_string)) #instead of using this we can use method below
my_string.lower()
print(my_string.lower())
print(my_string.upper())
print(my_string.capitalize())
print(my_string.title())
print(my_string.swapcase())

#Searching for a substring in a string
print(my_string.find('th')) #returns the index of the substring of the string.
print(my_string.find('gi'))#returns -1 if the substring is not found in the string(follow each other).
print(my_string.count('o'))#returns the number of times the substring appears in the string.


city='Mississippi'
print(city.count('iss'))#returns the number of times the substring appears in the string.

#cleaning up the string
my_string= "python Programming "

print(my_string)
clean = my_string.strip() #removes the white spaces
cleaned = my_string.lstrip() #removes the white spaces from the left
cleaned2 = my_string.rstrip() #removes the white spaces from the right
print(clean) #remove the white spaces from the string.
print(cleaned) #take string that has white space from left and remove it.

#VALIDATION.
file = "my_work.pdf"
if file .endswith('.pdf'): #method
    print("This is a pdf file")
else:    print("This is not a pdf file")#if it's not a pdf file, it will print this statement.

#same example as the above but with a different method.
age= "22"
if age.isdigit(): #method to check if the string is a digit or not.
    #age = int(age) #convert the string to an integer. whithout this line it still prints the output but it will be a string and not an integer.
    print(age)

    message= "I love programming. Python is the way to go in 2026"
    new_message= message.replace('love', 'hate') #replace method to replace a substring with another substring.
    print(new_message)

    #SPLITTING A STRING
    my_message = message.split() #split method to split the string into a list of words.
    print(my_message)

#delimiter 

    message= "I love programming. Python is the way to go in 2026"
    new_message= message.replace('love', 'hate') #replace method to replace a substring with another substring.
    print(new_message)
    my_message = message.split(" . ") #split method to split the string into a list of words.
    print(my_message)

    fruits = "apple, banana, orange, grape"
    my_fruits = fruits.split(" , ") #split method to split the string into a list of words using a delimiter.
    print(my_fruits)

    #JOIN
    
    language= ['J' , 'a' , 'v' , 'a' 's' , 'c' , 'r' , 'i' , 'p' , 't']
    print(''.join(language)) #join method to join the list of words into a string.

#CLEANING UP AN EMAIL ADDRESS
email= "   USER_Name@UT AC.UK  \n"
clean_email = email.strip().lower().replace('_', '.') #strip method to remove the white spaces and lower method and replace method to replace the underscore with a dot.
print(clean_email)
