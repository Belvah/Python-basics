#PEDMAS

a = [2,4,6] *2# to multiply each element in the list a by 2.
b = [3,5,7] 
c = a+b
print(c)

my_list=['Esther' , 'Nancy', 'Belvah', 'Grace']
names = ['Mutheu', 'Wanjiru'] #to add the names in the my_list.
print(my_list[1:2]) #to print the second element/slice in the list my_list. If we remove starting point it starts from Esther to Grace.
my_list.append('Cynthia') #to add Cynthia to the list my_list.
print(my_list)
my_list.extend(names) #to add/extend the names in the list names to the list my_list.
print(my_list)
my_list.sort()#to sort the names in the list names in alphabetical order.
print(my_list)
my_list.reverse() #to reverse the order of the names in the list my_list.
print(my_list)
rm_name = my_list.pop() #to remove the last element in the list my_list.LIFO. If we put 1 it will remove the second element in the list my_list.
print(my_list)
print(rm_name) #to print the name that was removed from the list my_list.
named = my_list.remove('Nancy')
print(my_list) #to print the list my_list after removing Nancy from the list my_list.

del my_list[1:3] #to delete the second and third element in the list my_list. If we put 1 it will delete the second element in the list my_list.
print(my_list) #to print the list my_list after deleting the second and third element in the list my_list.

numbers =[23, 13, 42, 89, 5, 67, 17,]
print(len(numbers)) #to print the length of the list numbers.
print(max(numbers)) #to print the maximum number in the list numbers.
print(min(numbers)) #to print the minimum number in the list numbers.
print(sum(numbers)) #to print the sum of the numbers in the list numbers.

#PROGRAM TO CALCULATE THE AVERAGE OF NUMBERS IN A LIST.
# my_num = []
# while True:
#     num = input("Enter a number \n")
#     if num == 'done':
#         break
#     all_nums = float(num) #data conversion.all_nums is the variable that will take the value of the number that the user will input.
#     my_num.append(all_nums) #to add the numbers in the list my_num.

# average = sum(my_num)/len(my_num) #to calculate the average of the numbers in the list my_num.
# print(f'The average of the numbers is: {average}') #to print the average of the numbers in the list my_num.

name = 'Mutheu'
my_list = list(name) #to convert the string name to a list my_list.
print(my_list) #to print the list my_list.

name= 'Esther'
my_name ="Esther"
print(my_name is name) #to check if the variable my_name is the same as the variable name. It will return true because they are the same.
