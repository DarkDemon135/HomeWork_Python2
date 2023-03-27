diapazon = int(input("Введите диапазон для поиска простых чисел: "))
for i in range(1,diapazon):
        count = 0
        delitel = 2
        while delitel < i:
            if i % delitel == 0:
                count += 1
            delitel += 1
        if count == 0:
            print (f'{i} простое число')
