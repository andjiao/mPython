# magic method are the methods that have two underscores at the beginning and end of their naame
#and they are called automatically by python interpreter depending on how we use oure objects and classes
#fx we have oure init magic method, we don't call it directly
#it's called automatically by python interpreter when we create a new Point-object

# for more info about magic methods: https://rszalski.github.io/magicmethods/


class Point:
    
    def __init__(self,x, y):
        self.x=x
        self.y=y
        
    def __str__(self):
        return f"({self.x}, {self.y})"
        
    def draw(self):
            print(f"Point ({self.x}, {self.y})")
            

p= Point(1,2)
#by default it returns the name of the class of this object, followed by it's memory address
p.__str__

print(p)

#we get the same result like the __str__, when converting to string
print(str(p))