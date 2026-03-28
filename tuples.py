my_tuple = ('Esther', 'Nancy', 'Belvah', 'Grace') #to create a tuple my_tuple.
new_tup = tuple(my_tuple)
print(new_tup) #to print the tuple new_tup.

print((2, 7, 9) < (4, 6, 8)) #to compare two tuples.

txt= 'but soft what light through yonder window breaks'
strings = txt.split() #to split the string txt into a list of strings.

my_words = list()
for word in strings:
    my_words.append((len(word), word)) #to add the length of each word and the word as a tuple in the list my_words.

my_words.sort(reverse=True) #to sort the list my_words in reverse order.

new_words = list()
for length, word in my_words:
    new_words.append(word) #to add the word in the list new_words.
print(new_words) #to print the list new_words.