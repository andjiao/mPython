list1 = [1, 2, 3]
list2 = [4, 5, 6, 7]

# zip combines two lists into one, we can't use map or comprehsion bc they only work with a single list
zip(list("abc", list1, list2))
