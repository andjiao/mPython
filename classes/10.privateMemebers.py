
class TagCloud():
  
    def __init__(self):
        #to change the name allover click f2 (in mac fn+f2)
        #to make the tags private or inaccessible from the outside, you need to preface it with 2 underlines
        #so this how we can make certain attributes or certain methods in the class private
        #if you prefix methods/attributes with two underscore, they are considered private 
        #having said that, technically these memeber are still accessible from the outside
        #it's just a littel bit harder to acces them 
        # so the point of this practice is not security, it's more of a warning or alert someone who is using this class
        #it's telling the consumer of the class, hey don't touch this, this is private 
        self.__tags = {}
    
    def add (self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(),0) +1
  
 
    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)
   
    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count
    
    def __len__(self):
        return len(self.__tags)
    
    
    def __iter__(self):
        return iter(self.__tags)

cloud = TagCloud()

#every class or every object has this property called __dict, this is a dictonary
#that holds all the attributes in this class

#so when python interpreter runs this code, it automatically rename this attributes and prefixes it with the name of it's classes

#so in python, unlike java, we don't really have the concept of private members, these private memebers
#these private members are still accessible from the outside 
#using double underscore is more of a convention to prevent accedental acces to these private members
cloud.__dict__()