letters = ['a', 'b', 'c', 'd']

# adding in the end
letters.append('d')

# adding an item at a specific position, 1 tells where to add item
letters.insert(1, 'hej')

# removing the last item, can also pass an index to remove item of an given index
# this one can only delete one item
letters.pop('b')

# if you don't know the index-numer you place it in paramete, but only the first occurence of b will be removed
letters.remove('b')


# here we can delete a range of items
del letters[0:3]

# removing all of it
letters.clear()
