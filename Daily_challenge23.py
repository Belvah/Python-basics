# Write a program that takes a string as input from the user and checks if it's a palindrome (reads the same backward as forward). Ignore case sensitivity and punctuation.

string = "ANNA"
string= "LOKI"
string = string.lower()

# Remove punctuation and spaces - keep only letters
cleaned = ""
for char in string:
    if char.isalpha():
        cleaned = cleaned + char

# Reverse the string using traversal
reversed_string = ""
for i in range(len(cleaned) - 1, -1, -1):
    reversed_string = reversed_string + cleaned[i]

if cleaned == reversed_string:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
