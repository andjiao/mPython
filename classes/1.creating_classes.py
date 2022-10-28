#in python we use pascal-convention, whicn means every first letter in a word should be uppercase 
#and should nit use unserscore to seperate words 

# to name oure variables and functins we use all lower case letters and seperate multiple words using an underscore


#colon indicates that theres is a block
class Point:
    #all functions in oure classes should have at least one parameter 
    #and by convetion we call that parameter self
    def draw(self):
        print("draw")


#to create a point object, we call the class like a function

p= Point()

#if we use the dot-operator, you can see we have a draw-method as well as a bunch of other methods
#that we didn't define, but oure point object got this method from another object in python 
#through a mechanisme called inheritance 


#sometimes we have an object and we want to know if this object is an instance of a given class 
#it will return true if it an instance
isinstance(p, Point)