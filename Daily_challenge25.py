# Write a program that opens a text file and iterates through each line using a for loop, printing each line separately.

file = open("mbox.txt", "r")

for line in file:
    print(line.strip())

file.close()
