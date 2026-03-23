# #WHILE LOOP
# #initialization step

# num=10
# while num>0:
#     print(num)
#     #incremental step
#     num=num-1

#     print('Finished looping!')

#     #check example of an infinite loop
#     num=1000
# while num>0:
#     if num==800: #gives control to the loop
#         break
#     print(num)
#     #incremental step
#     num=num-1

#     print('Finished looping!')

    #another example of an infinite loop
# word= 'python'
# while True:
#         guess=input("Which is the most popular programming language in 2026?")
#         if guess=='':
#             print('please enter a valid guess')
#             continue
#         if guess == word:
#             print('Congratulations! You guessed it right!')
#             break
#         print('Nice attempt, please try again another time.')

#guess the number 3 using integers
number = 2
while True:
        guess = input("Which one is an even number?")
        if guess == '':
            print('Please enter a valid number between 1 and 3.')
            continue
        guess = int(guess)
        if guess == number:
            print('Congratulations! You got it right!')
            break
        print('Wrong attempt, try again.')