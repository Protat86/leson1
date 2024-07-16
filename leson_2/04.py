def get_middle_three_chars(s):
    # Перевірка, чи довжина рядка достатня для отримання трьох середніх символів
    if len(s) < 3:
        return "Рядок занадто короткий для отримання трьох середніх символів"
    
    # Знаходження середнього індексу
    middle_index = len(s) // 2
    
    # Витягування трьох середніх символів
    new_str = s[middle_index - 1: middle_index + 2]
    
    return new_str

# Введення вхідних даних для двох випадків
str1 = "JhonDipPeta"
str2 = "JaSonAy"

# Виведення результатів
print(f"Вхідні дані: {str1}")
print(f"Вихідні дані: {get_middle_three_chars(str1)}")
print(f"Вхідні дані: {str2}")
print(f"Вихідні дані: {get_middle_three_chars(str2)}")
