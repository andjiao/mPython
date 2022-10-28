class Point:
    
    def __init__(self,x, y):
        self.x=x
        self.y=y
        
    def __eq__(self, other):
        #so if this expression is evaluated to true 
        #these two objects are considered equal
        return self.x == other.x and self.y == other.y
    
   
    def __gt__(self, other):
        #so if this expression is evaluated to true 
        #these two objects are considered equal
        return self.x > other.x and self.y > other.y
    
    

p = Point(1,2)
another = Point(1,2)

#by default this equality operator compares the reference or addresses of these two objects in memory 
# in this case, the two variables are refereing two different objects in memory 
# and that's why they are not equal 
print(p == another)

 #the greater sign is not supported btw two instances of the point class 
 #to make the code below to work, we have to define a magic method in the class
print(p > another)

# when you implement the greater than magic method, python will 
# automatically figure out what to do if you use the less operator 
print(p < another)

