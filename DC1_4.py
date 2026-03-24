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
    

    #Write a function called calculate_grade that takes a score as input and returns the corresponding letter grade (A, B, C, D, F) based on a grading scale (e.g., A: 90-100, B: 80-89, etc.).

        def calculate_grade(score):
            """A function that calculates grades based on input scores """
            if score >100 or score < 0:
                return "Invalid score"
            
        #conditional logic for grading A,B,C,D,E
            elif score >= 90:
                return 'A'
            elif score >= 80:
                return 'B'
            elif score >= 70:
                return 'C'
            elif score >= 60:
                return 'D'
            else:
                return 'E'
            
        try:
            user_score=float(input("Enter the student's score:\n"))
            grade=calculate_grade(user_score)
            print(f'Your grade is: {grade}')
        except ValueError:
            print("Please enter a valid")