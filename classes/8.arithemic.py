class Point:
    
    def __init__(self,x, y):
        self.x=x
        self.y=y
        
    def __add__(self, other):
        return Point (self.x + other.x, self.y + other.y)


p = Point(10,20)
another = Point(1,2)

print(p > another)

#to get the result printet out, we need to store the result in a variable

combined = p + another

print(combined)