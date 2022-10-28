letters = ['a', 'b', 'c', 'd']

letters[0] = 'A'

# -1 betyder det første bogstav bagfra
letters[-1]

# slicing,
# when slicing a string we can also pass a step [::2] (which is the thirds argument in slicing)
# it is useful when you eant to return every second or every third element in the orginal list

letters[0:3]

numbers = list(range(20))
print(numbers[::2])
