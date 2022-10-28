letters = ['a', 'b', 'c', 'd']


# enumerate makes the list a tuple,tuple is a list but it's read only, we csn't change the list
# enumerate is used to get the index
for letter in enumerate(letters):
    print(letter)

# a tuples is defined like a list but with parathese instedet of square bracket
items = (1, 'a')
