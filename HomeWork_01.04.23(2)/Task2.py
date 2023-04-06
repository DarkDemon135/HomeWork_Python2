cifri = "0123456789"
bykvi = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz"
c = 0
b = 0
s = input("Введите строку: ")
for i in s:
    if i in cifri:
        c += 1
print(f"Количество цифр в строке {c}")
for i in s:
    if i in bykvi:
        b += 1
print(f"Количество букв в строке {b}")