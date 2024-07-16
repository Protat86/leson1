str1 = input("Введіть рядок: ")
str1 = str1.lower()
is_palindrome = True
length = len(str1)
for i in range(length // 2):
    if str1[i] != str1[length - i - 1]:
        is_palindrome = False
        break

if is_palindrome:
    print("The entered string is palindrome")
else:
    print("The entered string is not palindrome")
