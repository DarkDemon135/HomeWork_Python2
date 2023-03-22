count = 0;
number1 = 0
number10 = 0
number100 = 0
for i in range(100, 999):
    number100 = i / 100
    number10 = i / 10 % 10
    number1 = i % 10
    if (number1 == number10 and number10 == number100 and number1 == number100):
        count += 1
        print("Such numbers ", count )