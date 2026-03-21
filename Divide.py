def simple_division():
     try:
          # Handling dangerous code
          number = int(input("please enter a number to divide by ten "))
          result = 10 / number
          print(f"The answer is {result}")
     except:
          # Handle the error
          print("oops! cannot divide the number")

simple_division() #call the function


