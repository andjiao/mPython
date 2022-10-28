class Point:
    default_color ="red"
    def __init__(self,x, y):
        self.x=x
        self.y=y
        
        #cls is short for class, this is convention, you can call this anything
        #but by convention, whenever we define a class method we call its first parameter for cls
        #and it's a reference to the class itself 
        
        #to make this method a class method we need to decorate it
        #the @classmethod is called a decorator
        #and it's a way to extend ther behavior of a method or function
        @classmethod
        def zero(cls):
            #this is like calling Point(0,0)
            #when using cls at runtime when we call the zero-method 
            #python interpreter will automatically pass a reference to the point class to the zero-method
            return cls(0,0)
            
        def draw(self):
            print(f"Point ({self.x}, {self.y})")
        


Point.default_color= "yellow"      
p= Point(0,0)

#you use these instance methods whenever we need an object reference 
#fx when drawing a point, you really need to work with a specific point object
#that is why this draw method is defined as an instance method 
#but there are times that you don't really need an existing object and that's when we use a class method
#fx let say in oure program there 
p.draw()

# when starting with upper-case, it's a class-reference which means i'm working on class-level
#so the zero is a method that is defined on a class-level 
#and when we call it, it will return a point object initialized with the values set on line 12

#we refer to this zero method as a factory method bc it's like a factory, it creates a new object
# so this zero methods takes the values that has beeen set on line 12 
p = Point.zero()

p.z=10


another = Point(3,4)

