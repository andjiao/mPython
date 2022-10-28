
class Point:
    
    #defining a class-level attribute 
    default_color ="red"
    def __init__(self,x, y):
        self.x=x
        self.y=y
        def draw(self):
            print(f"Point ({self.x}, {self.y})")
        

# changing the attribute-value, the change is visible to all object of thar type 
#try to comme-out the line underneath to see
Point.default_color= "yellow"      
p= Point(1,2)

#we can also define an attribute after we have created a point object
#bc objects in python are dynamic like in js 
#so we don't have to define alle the attributes in the constructor, we can define them later, whenever we need them 
p.z=10

#alle the attributes we have defined, x,y and z, these are instances attributes 
# in other words these are atrributes that belongs to p-instances or p-object 
# so every point object can have different values for these attributes 

#each point-object has it's own attributes-values
another = Point(3,4)

#but we can also define class attributes adn these are attributes we define at the class level 
#and they are the same across all instances of the class 
#as a metaphore we can say, that all humans has two eyes and two ears
# sot these are the attributes defined at the class level and they are shared among all instances 