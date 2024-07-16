def sort_by_indexes(a, b, reverse=False):
    combined = zip(b, a)
    sorted_combined = sorted(combined, reverse=reverse)
    return [item[1] for item in sorted_combined]

a = ['eggs', 'bread', 'oranges', 'jam', 'apples', 'milk']
b = [3, 2, 6, 4, 1, 5]

print(sort_by_indexes(a, b)) 

print(sort_by_indexes(a, b, reverse=True)) 

