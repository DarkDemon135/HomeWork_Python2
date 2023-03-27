ans = 0
for i in range(100, 1000):
    a, b, c = str(i)
    if a==b or a==c or b==c:
        ans += 1
print(ans)