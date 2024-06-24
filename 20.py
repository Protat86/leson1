seconds = int(input("Введіть кількість секунд: "))

days = seconds // (24 * 3600)
hours = (seconds % (24 * 3600)) // 3600
minutes = (seconds % 3600) // 60
remaining_seconds = seconds % 60

print("Дні:", days)
print("Години:", hours)
print("Хвилини:", minutes)
print("Секунди:", remaining_seconds)
