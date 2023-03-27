b = 3
n = 5
i = 1
while i <= n:
    j = b
    while j <= n:
        print(i * j, end="\t")
        j += 1
    i += 1
    print()