def check_num(n):
    digs=[0]*10
    while n>0:
        k=n%10
        if digs[k]>0:
            return False
        digs[k]=1
        n=n//10
    return True
def task():
    c=0
    for i in range(100,10000):
        if check_num(i):
            c+=1
    return c
    
print(task())