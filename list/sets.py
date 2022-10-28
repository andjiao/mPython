# set is a collection with no duplicates 

numbers =[1,1,1,1,2,2,2,3,4,5,6,7]

# if you want to remove the duplicaate ypu can convert this to a set 

uniques = set(numbers)

# we use curly brackets to define sets 
second ={1,2}
second.add(4)
second.remove(4)
len(second)

# but where sets shine is the powerful math-operation that are supported by them 

first = set(numbers)
second = {1,2}

# now we can get an union of two sets, using the vertical bar 
# return a new set that includes all the items that are either in the first or second set (union)

first | second

# so the union of the two sets is another set that include alle the items that are that are either in the first or second set 

# we can also get the intersection of two sets 
# this will return a new set, that includes all the items that are in both first and second
#  returns the element that exist in both sets 
print(first & second)

# we can also get the difference btw the two sets 
# returns the additional number from first-set that we have in one of the sets, that the don't have 
print(first - second)


# we also have semanctic difference 
# returns the items that are either in the first or second, but not in both 
print(first ^second) 

# unlike lists, there are an unordered collection, 
# which means that the items that we have in a set are not in sequence, so we cannot acces them using an index
# but we can check for the existence of an item in set 

if 1 in first:
    print("yes")
    
# set is a collection of unique items, we cannot have duplicaates and this object are unordered, they are not in sequence 
# so we cannot acces them using an index