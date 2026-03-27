
data = 'From stephen.marqued@co.ke Sat Feb 23 20:32:45 2021'
start_at = data.find ('@')
print (start_at) #to know index of @

#variable to store the email address
space = data.find(' ', start_at) #to find the index of space after @
host = data[start_at+1:space] #to extract the host name
print(host)

#STRING FORMATTING. f-strings are used to format strings in Python. They allow you to embed expressions inside string literals, using curly braces {}.
name= "Joseph"
print (f" Welcome {name} to the world of Python programming") #f string to print the name in the welcome message

#formatting numbers using f-strings. You can specify the number of decimal places to display for a floating-point number using the :.2f format specifier, which rounds the number to 2 decimal places.
price = 589.8765
print (f"The price of the item is {price:.2f}") #f string to format the price to 2 decimal places

import os

if os.path.exists("mbox.txt"):
    print("File exists")
    print(f" The file is: {os. path.getsize('mbox.txt')} bytes") #f string to print the size of the file in bytes   
else: 
    print("File does not exist")   
    print(f'current directory: {os.getcwd()}') #f string to print the current working directory

    # #mode -w,r,a
    # fhand= open("mbox.txt", "r") #open the file in read mode
    # data = fhand.read() #read the contents of the file and store it in a variable called data   
    # print(data) #to print the file handle
    # fhand.close() #to close the file handle

    with open('mbox.txt', 'r', encoding='utf-8') as fhand: #open the file in read mode using with statement
        data = fhand.read() #read the contents of the file and store it in a variable called data
        print(f'The length of the file is: {len(data)} characters') #to print the length of the file        


