# a tuple is a read only list 
# we can use it to contain a sequence of objects, but we can not modify the sequence 
# we can not modify a new object to it, we cannot remove an existing object aand we cannot 

# instead of square-bracket we use paranthesis to define a tuple 

# if you have one item, you should add a training comma, otherwise python thinks you're defining an integer 

# if yoy want to define an empty tuple, use empty paranthesis 

# we can slo convert a list to a tuple, to do that we call the tuple-function

p1 = (1,2,3)
p2 = tuple([1,2]) 
p3 = tuple("Hello world") 

#we can acces individual items using an index 
p1[0]
#or we caan get a range of items, this returns aanother tuple 

p1[0:2]

#we can also unpack tuples, but tuples are immuteable, we can note mutate them (which means we cannot change them )
x,y,z = p1
if 10 in p1:
    print("exist")
    
# lets say you are dealing with a sequence of objects aand you want to make suree that you don't accedentily modify this sequence, add new object

 