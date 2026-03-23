#Create a function that will determine whether a number is positive or negative.

def check_number(num):
    if num > 0:
        print(f'{num} is positive')
    elif num < 0:
        print(f'{num} is negative')
    else:
        print(f'{num} is zero')

while True:
    user_input = input("Enter a number: ")
    if user_input == '':
        print('Please enter a valid number.')
        continue
    check_number(int(user_input))


    #Write functions to calculate the area of different shapes like square (area_of_square(side_length)), rectangle (area_of_rectangle(length, width)), and circle (area_of_circle(radius)).

    import math
    def area_of_square(side_length):
        return side_length*side_length
    def area_of_rectangle(length, width):
        return length*width
    def area_of_circle(radius):
        return math.pi*radius**2