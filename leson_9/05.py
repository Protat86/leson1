def average_by(lst, fn=lambda x: x):
    if not lst:
        raise ValueError("Список не може бути порожнім.")
    mapped_values = map(fn, lst)
    total = sum(mapped_values)
    return total / len(lst)

lst = [{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }]
result = average_by(lst, lambda x: x['n'])
print(result)




