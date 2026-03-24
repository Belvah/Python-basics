# word='banana'
# number='45'
# print(type(number))
# print(word[4])
#  #prints the 4th index of the word 'banana' which is 'n'
# print(word[2.5])
# #prints the length of the word 'banana' which is 6
# #To get last index of the word we can use -1
# print(len(word))
# last_index=len(word)-1
# print(word[last_index])

#Slicing-creates a substring
#[starting: stopping:]

message = "welcome to python programming"
print(len(message))
print (message[0:10]) #start from index 0 and stop at index 10
print (message[5:])#start from index 5 and go to the end of the string
print(message[:])#print the whole string/creates copy of the string

number='0725439354'
print(number[0::3]) #start from index 0 and print every 3rd character
print(number[0:3]) #start from index 0 and stop at index 3
print(number[::-1]) #reverse the string
#message[1]='i' #strings are immutable, we cannot change a character in a string
language='pithon'
Corrected=language[0] + 'y' + language[2:]
print(Corrected)