numbers = [1, 2, 3, 4, 5, 6, 6]

# it we want to sort the list in a descent order we use the reverse-key-word
# this one modify the original
numbers.sort(reverse=True)

# this return a new list in correct order
sorted(numbers)


items = [
    ('produkt1', 10),
    ('produkt2', 30),
    ('produkt3', 20),
]
# to sort a tuple


def sort_item(item):
    return item[1]


# first argument is a key, here we pass function
# when python attempt to sort this item, it will get each item and then pass each item to our sort-function
# bc it takes key as argument we have to use keyword key
items.sort(key=sort_item)
