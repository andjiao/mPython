course = "Python programming"

#We have triple quotes, using them for long strings
message = """
Det er sommer
det er sol 
og det er søndag
alle er så glade og fri
"""

# funtion is a reusable piece of code that carries out a task. 
# In python we have funtions that areb build into the language, we can reuse them to perform various tasks

#len bruges til at få længen af en string

#whenever using funtion use parathesis, and now you are calling aa funtion, which means you are using this funtion.
#arguments are inputs to funtion

print(len(course))

print(course[1])
print(course[-2])
#if you want to extract the first 3 character in a string, first is startindex, and second is
#this return aaf new string 
print(course[0:3])
#this wil return a new string that are the same to the original string
print(course[0:])

print(course[:3])
print(course[:])