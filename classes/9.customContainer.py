#with this class we are encaplsulating the complexity around the case-sensitivy of the tags 
#when using classes we no longer haave to worry about lowercase or uppercase characters 
#all that complexity is encapsulated in the TagCloud-class 
#it is not visible to the rest of oure program
class TagCloud():
    #making constructor
    def __init__(self):
        #we initialize tags attributes to an empty dictonary
        self.tags = {}
    
    def add (self, tag):
        # we check to see, if we have this tag in oure dictonary
        #if we don't we're going to set it's value to 1
        #ptherwise we're going to increment it by 1
        
        # we use the get, to get an item by this key called tag, and supply a default value if we don't have them(which is zero)
        # so the self.tags.get(tag,0) is the count we get and increment it by one 
        #and we set the value for this key 
        # to make sure it does not differentciate btw Python and python, we convert the tags to lowercase
        #this would not be possible if we just use a standard dictonary 
        self.tags[tag.lower()] = self.tags.get(tag.lower(),0) +1
    
    #def __getitem__(self, key):
    
    #if we don't have the python tag oure dictonary would throw an error 
    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)
    
    #this method takes 3 parameters: def __setitem__(self, key, value)
    #with this implementation we can set the number of a given tag 
    
   
    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count
    
    def __len__(self):
        return len(self.tags)
    
    #to make this iterable, to iterate over a for loop we need to implement another magic method
    def __iter__(self):
        # now we have to use one of the build in functions to get an iterate object
        #an iterator object it an object that wants a container and gets one item at a time
        #so iter is a built in function, adn we want to iterate through tags
        #this function returns an iterator object which is gives us one item at a time in a for loops 
        return iter(self.tags)
        
        

cloud = TagCloud()
# I want to be able to read the count of a tag, to do the code below, we need to implement a magic method called getItem

cloud["python"]
 #in order to get the number of items in this tag cloud, we should implement the len magic method
len(cloud)
cloud.add("python")
cloud.add("python")
cloud.add("python")

print(cloud.tags)