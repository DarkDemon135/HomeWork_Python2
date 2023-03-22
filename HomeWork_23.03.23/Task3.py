while True:
    n = int(input())
    if n > 0 and n != 7:
        print("Number is positive")
    if n < 0:
        print("Number is negative")
    if n == 0:
        print("Number is equal to zero")
    if n == 7:
        print("Good bye!")
        break