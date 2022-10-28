numbers = [1, 2, 3, 4, 5, 6, 6]

numbers.sort(reverse=True)


sorted(numbers)


items = [
    ('produkt1', 10),
    ('produkt2', 30),
    ('produkt3', 20),
]


# items.sort(key = lambda parameters:expression) - syntax for lambda
# parameters, what are the arguments
# expression, what will we return

items.sort(key=lambda item: item[1])
