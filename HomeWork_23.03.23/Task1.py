a=int(input())
b=int(input())
s1=0
s2=0
s9=0
for i in range(a,b+1):
    if i%2!=0:
        s1+=i
    if i%2==0:
        s2+=i
    if i%9==0:
        s9+=i
print("Сумма нечетных: ",s1)
print("Сумма четных: ",s2)
print("Сумма кратных 9: ",s9)