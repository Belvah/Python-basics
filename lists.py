veges = []
print(type(veges))

data= [23, 45, ["french-fries", "burger"], {'name': 'Jane'}, True, False]
#data[1] = 'Grace' #commenting out so that it can return 45 as true not false.
#print(data)

print(45 in data) #xchecking if 45 is in the data above.

for x in data: # List comprehension.
    print(x)



numbers= [2, 3, 4, 5, 6, 7, 8, ]

#for number in numbers: #number is the variable that will take the value of each element in the list numbers.
for number in range(len(numbers)): #n -1 #to check range of numbers.
    numbers[number] = numbers[number] **3  #to multiply each element in the list numbers by 3.
print(numbers)


