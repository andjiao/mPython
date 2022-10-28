items = [
    ('produkt1', 10),
    ('produkt2', 30),
    ('produkt3', 20),
]

# in python we have anotther feature for achivieving the same result as filter
# syntax for comprehsion  [expression for item in items]
# expression it what we want, here we want the price, therefor the expression is item[1]
# comprehsion produce exact same result as map aand filter

# the code underneact produce same as map
f = [item for item in items]

# the code underneact produce same as filter
filtered = [item for item in items if item]
print(filtered)
