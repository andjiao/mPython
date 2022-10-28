# in python we have some funtions connected to string, whoch is called methods

# everything in python is an object and every object have funtions which we call methods

course = "Python programming"
print(course.upper())
print(course.lower())

# transform the first letter in every word tol uppercase
print(course.title())

# removes white space in the right, while strip removes every white space
print(course.rstrip())

# if returning -1 means it does not exist in the original string. This one returns the index of these characters
print(course.find("pro"))
print(course.replace("p", "j"))

# this checks if we have pro in course. This one returns a boolean
print("pro" in course)

# this one will return true, bc seit is not in the course
print("seift" not in course)
