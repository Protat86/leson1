n = int(input("Введіть кількість хвилин: "))
hours = (n // 60) % 24
minutes = n % 60
print(hours, minutes)
