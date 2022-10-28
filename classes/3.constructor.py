#constructore is a speciel method that is called when when we create a new Point object 


class Point:
    
    #this is a special method that we call a magic method
    #in python classes we have severel. So this magic method here, is called a constructore 
    #and it is executed when we create a new point object 
    #all methods that we define in classes should have at least one parameter which we call self by convention 
    # and optinally we add any addiotnal parameters for initializing oure point object 
    
    
    #self is a reference to a current point-object fx here in line 12 when we call the point class 
    #python will internally create the point-object in memory and set itself to reference that point object 
    
  
    def __init__(self,x, y):
        #setting default value
        #self.x = 0
        
        #or we can set this x argument that we recieve in this method
        self.x=x
        self.y=y
        
        # so self means we have a reference to the current object and with that
        #we can read the x and y values  
    def draw(self):
        #so using self we can read attributes of the current object 
        # or we can also call other methods in this object 
        print(f"Point ({self.x}, {self.y})")
        
        
p= Point(1,2)

#attributes are variables that include data about that object
#fx we can have attributes like x and y 
#in other words, class or an object bundles data and functions elated to hat data into one unit
#once again, as a metaphor, think of a human. The human can have attributes like eye color, height, weight etc.
#as well as functions as walk, talk etc.

print(p.x)

# when calling this method, we did not have to supply a value for the self parameter
#bc python does that by default 
p.draw()

