#dictonary is a collection of key value pairs
# we use it to map a key and value 

#fx a phone book, here we map a person's name to their contact detail 

# so we use the persons name as the key and their contact infor as the vaalue 
# so the phone book is a dictonary, it's a collection of key-value-pair 

# here the key is the string and value the integer
# in python we can only use immutable types, so quite often we use strings and numbers 
# but the value can be any types, no limits 
point ={"x": 2, "y":3}

# we can also use the dict function, to create a dictonary 
# so when we call this function we pass one or more keyword arguments fx x=1 is a keyargument
point = dict(x=1,y=2)

#we can get the valu associated with a key using an index 
# the index is the name of a key 
# bc dicts are collections of key value pairs, we cannot acces them, using a numerate index 

print(point["x"])

# we can change the vaalue of the key
point["x"] =10

#adding new key
point["z"] =20

#check an element exist
if "a" in point:
    print(point["a"])
    
# other wey to check, using get-method
# so if the key does not exists it returns none

print(point.get("a"))

# or we can pass a default value as an argument
# so here we say, if don't have the key a return 0 by default 
print(point.get("a", 0))

# to delete an item
del point["x"]

# looping to get only keys

for x in point:
     print(x)

#looping to get both key and value
for key in point:
     print(point[key])

#another way to loop dict
# it returns a tuple where we have a key and a value

for x in point.items:
     print(x)

#unpacking
for key, value in point.items():
     print(key, value)