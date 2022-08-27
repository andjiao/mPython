#range is how many times we want to repeat
#for number in range(3):

#saying it should start from nr.1 and stop at 4
#for number in range(1,4):
    
for number in range(1,10,2):
    #here we wrie alle the statements that should be repaeated 3 times 
    print("hej", number + 1, (number +1) * "t" )
    

n = 100
while n >0:
    print(n)
    #this is called the augemnted assignment, when you put ligmed og logical sammen, altså plus, minus divider osv.
    n //= 2
    
    
    #only run this in terminal
    #when using lower, whatever userInput is, it will be converted to lower-case 
    # and then no matter how user writes quites, it will match with the condition, where quite is quit is written in lowercase
    command = ""
    while command.lower != "quit":
        command = input("<")
        print ("ECHO", command)
        

while True:
    command = input("<")
    print("ECHO", command)
    if command.lower() == "quit":
        break
    