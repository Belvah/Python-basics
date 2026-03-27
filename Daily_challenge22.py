# Create a program that checks if two given strings are anagrams of each other.

string1 = input("Enter the first string: ").lower()
string2 = input("Enter the second string: ").lower()

# Check if they have the same length first
if len(string1) != len(string2):
    print("The two strings are not anagrams of each other.")
else:
    # Count each letter in string1
    is_anagram = True
    for char in string1:
        if string1.count(char) != string2.count(char):
            is_anagram = False
            break

    if is_anagram:
        print("The two strings are anagrams of each other.")
    else:
        print("The two strings are not anagrams of each other.")
