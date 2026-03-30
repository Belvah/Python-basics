#Store students' IDs.

students_ids = {201, 202, 203, 204,}
my_set = {1, 'Joseph', 2.5, (500, 101) }
print(type(my_set))#prints <class 'set'> as the type of my_set is set.

#initialized as dictionary
my_students = {} #prints <class 'dict'> as the type of my_students is dictionary.
#print(type(my_students))--prints a dictionary as type.


my_students = set() #prints <class 'set'> as the type of my_students is set.
print(type(my_students)) #prints <class 'set'> as the type of my_students is set.


#my_hash = {2, 'Nancy', 3.8, ['Grace' , 'Esther', 909]} #prints TypeError: unhashable type: 'list' as lists are not hashable and cannot be added to a set.
my_hash = {2, 'Nancy', 3.8, ('Grace' , 'Esther', 909)} #prints <class 'set'> as the type of my_hash is set. Tuples are hashable and can be added to a set.
print(type(my_hash))

#CRUD OPERATIONS

my_hash.add('Belvah') #adds 'Belvah' to the set my_hash
print(my_hash) #prints the updated set with 'Belvah' added
my_hash.update ('Belvah')#adds 'Belvah' to the set my_hash again. Note that sets do not allow duplicate values, so 'Belvah' will only be added once.
my_hash.update ('Belvah', 'Cynthia')# Adds 'Belvah' and 'Cynthia' to the set my_hash. Note that sets do not allow duplicate values, so 'Belvah' will only be added once, but 'Cynthia' will be added.
print(my_hash) #prints the updated set with 'Belvah' added again. Note that sets do not allow duplicate values, so 'Belvah' will only be added once.

#To delete we use pop(FIFO)
Popped = my_hash.pop() 
print(Popped) #prints the element that was removed from the set

#OR operator-picks one of duplicates.

a = {1,2}
b = {2,3}
print(a | b) #prints the union of sets a and b, which is {1, 2, 3}.
print(a.union(b)) #prints the union of sets a and b, which is {1, 2, 3}.

#AND operator-picks common elements in both sets.

print(a & b) #prints the intersection of sets a and b, which is {2}.
print(a.intersection(b)) #prints the intersection of sets a and b, which is {2}.

#Subtraction operator-picks elements in one set but not in the other.

print(a - b) #prints the difference of sets a and b, which is {1}.
print(b - a) #prints the difference of sets b and a, which is {3}.

#^ operator-picks elements that are in either set but not in both./

print(a ^ b) #prints the symmetric difference of sets a and b, which is {1, 3}.
print(a.symmetric_difference(b)) #prints the symmetric difference of sets a and b, which is {1, 3}.

a= {1,2 }
b = {1, 2, 3, 4, 5}
print(a.issubset(b)) #prints True as set a is a subset of set b.
print(b.issuperset(a)) #prints True as set b is a superset of set a.
print(a.isdisjoint(b)) #prints False as set a and set b are not disjoint, they have common elements (1 and 2).  