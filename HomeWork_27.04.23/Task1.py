import random
 
rand_list=[]
n=10
from random import randint
 
rand_list = []
while len(rand_list) < 5:
    x = randint(1, 101)
    if x not in rand_list:
        rand_list.append(x)
 
print(*rand_list)

target = int(input("Введите число target: "))

def twoSum(rand_list, target):
    answer = 'В массиве нет такой пары чисел'
    for i in range(len(rand_list) - 1):
        for j in range(i + 1, len(rand_list)):
            if target == rand_list[i] + rand_list[j]:
                answer = 'Индексы чисел, которые в сумме дают target: ' + str(i) + ' и ' + str(j)
    return answer
print(twoSum(rand_list, target))