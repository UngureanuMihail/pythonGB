my_list = [1, 2, 3, 5, 6, 1, 2, 13, 16, 13, 5]
dublicated = list(set([x for x in my_list if my_list.count(x) > 1]))
print(dublicated)
