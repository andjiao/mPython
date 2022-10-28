values =[]

for x in range[5]:
    values.append(x*2)
    
#syntax for list comprehension
# [expression for item in items]
# so we iterate over an iterable in each oteration we get this item and then do something with it

# here the iterable is the range object that is returned from the range function 
#loop variable is x 
# and oure expression is x*2
# code below is identical to the code on top
# this comprehension can also we used with sets and dict
values = [ x*2 for x in range(5)]

#comprehension in set using curly brackets
v2 = { x*2 for x in range(5)}

# the difference syntax for sets and dict
# in sets we just haave values 
# and in dicts we have key value pairs that are seperated by colon, where we map

v3 = {1:"a", 2:"b"}

#to use comprehension expression to create dict objects by changing the expression
v4 = { x:x *2 for x in range(5)}

#the code below are the same as the code above
values ={}
for x in range(5):
    values[x] =x*2
    



