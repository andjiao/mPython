items = [
    ('produkt1', 10),
    ('produkt2', 30),
    ('produkt3', 20),
]

# let's say we want to filter this list and only get the items wirth prize greater than or equal to 10
# the result of the last expression item[1]>=10 will be boolean, if it is true, the item[1] will be returned
filteredList = list(filter(lambda item: item[1] >= 10, items))
