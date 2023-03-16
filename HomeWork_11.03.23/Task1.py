print("Сложение + ")
print("Произведение *")
while True:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    c = float(input("Введите третье число: "))
    operator = input("Выберите операцию: ")
    if operator == '+':
        n = a + b + c
        print(n)
        continue
    if operator == '*':
        n = a * b * c
        print(n)
        continue