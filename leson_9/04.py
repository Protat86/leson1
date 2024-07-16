def average(*args):
    if len(args) == 0:
        raise ValueError("Принаймні одне число має бути подане.")
    return sum(args) / len(args)

print(average(1, 2, 3)) 
print(average(*[1, 2, 3])) 


