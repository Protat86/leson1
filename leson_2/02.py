# Введення вхідного рядка
str1 = input("Введіть рядок: ")

# Перевірка, чи є довжина рядка парною
if len(str1) % 2 == 0:
    # Розбиття рядка на дві половини
    mid_index = len(str1) // 2
    first_half = str1[:mid_index]
    second_half = str1[mid_index:]
    
    # Перевірка, чи обидві половини однакові
    if first_half == second_half:
        print("The entered string is symmetrical")
    else:
        print("The entered string is not symmetrical")
else:
    print("The entered string is not symmetrical (length is not even)")
