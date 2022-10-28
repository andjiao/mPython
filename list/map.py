items = [
    ('produkt1', 10),
    ('produkt2', 30),
    ('produkt3', 20),
]

# let say we are only interested in the price of the items
# so we want to transform the list into a list of numbers/prices
# map function apply lambda function on each item of the list
# map will iterate over items and will call the lambda function on each item of the items
# list function tranforms items to a list

#x = map(lambda item: item[1], items)
#for item in x:        print(item)

prices = list(map(lambda item: item[1], items))
