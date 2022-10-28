numbers = [1, 2, 3, 4, 5, 6, 6]

# this line is the same as the code down below
# this is what we call list unpacking
# the number of variables we have on the left of the silet operator, should be equal to the number of items we have in the list
#first, second, third = numbers

# can be used when we have a lot of items, and do not want to write them all down
# when we prefix a parameter wit star, python will get all these arbitrary arguments and pack them into a list
first, second, *other = numbers

first = numbers[0]
second = numbers[1]
third = numbers[2]
