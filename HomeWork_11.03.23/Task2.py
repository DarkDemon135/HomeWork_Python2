a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
all = [a, b, c]
n = int(input("Выберите действие: \n1 - найти максимум \n2 - найти минимум \n3 - найти среднее \n"))
if n == 1:
    print ('Максимум из 3х:', max(all))
elif n == 2:
    print ('Минимум из 3х:', min(all))
elif n == 3:
    print('Среднее из 3х:', sum(all) / len(all))
else:
    print("Введите число от 1 до 3")