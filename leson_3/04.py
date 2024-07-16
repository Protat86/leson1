def includes_any(lst, values):
    return any(value in lst for value in values)

print(includes_any([1, 2, 3, 4], [2, 9]))  
print(includes_any([1, 2, 3, 4], [8, 9]))  
