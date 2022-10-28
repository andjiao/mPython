# to use an array in python we need to import it from the array module 

# the from array is a module an the import array is a class we have in the module
from array import array

## typecode is a string that determenes the type of objects in your array
# it is a string of one character thaat determenes the type of object in your list 
# and the second argument is a list 
array("i", [1,2,3,4])

# and similiar to list we have 

#however the objects in this array are typed, so here every object should be an integer or else we will get an error 

# only use array when dealing with a large sequence of numbers and you encounter perfomarnce problems, for other cases use list and tuples