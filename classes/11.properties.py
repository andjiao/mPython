#goal: price cannot be negative
from itertools import product


# when saying that a code is not pythonic, that means it is not using python best practices
#it's not using python's features to the best potentiel 

#here in python we use the property-buildin-function.
# a property is an object, that sits in front of an attribute and allows us to get or set valeu of the attribute 
class Product:
    def _init_(self, price):
        #when running program, our data validation from set-function will kick in
        #and it will throw an exception
        
        #bc of the property-decorater we can use the property as a regular property
        self.price = price
      
      # since we have made it a property the get_price is not an ideal name, so we change it to price  
    # when python interpreter sees the l 19-21
    # it will automaatically create a property object called price  
    @property
    def price(self):
            return self.__price
        
        # here this decorater start with the name of the property, in this case price
    @price.setter
    def price (self, value):
            if value <0:
                raise ValueError("Price cannot be negative")
            self.__price = value
            
            
# here we define a class attribute with an ideal name

#calling the built in property function
#this function takes four params and all these params are optional
#the first param is a function for getting the value of an attribute 
#the second param is a function for setting the value of the attribute
#the third param is a function deleting that attribute 
#and last is for documentation

#note that the funcrions are not called, only passing a simple reference to them
#so when we call the buildin property function with these arguments 
#this function will return a property object, that property object will use the get_price-function 
#for getting the value of the price attribute

#instead of explicit call the property function to create property object
#we can apply the property decorater to the get-method
    #price = property (get_price, set_price)


# so the property looks like a regular attribute from thge outside
#but internaally it has two methods that we call a getter and setter         
product = Product(10)
print(product.price)
            