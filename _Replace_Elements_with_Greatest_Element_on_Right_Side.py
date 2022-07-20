a=int(input())
c=list(map(int,input().split()))
b=[]
d=[]
for i in c:
    d.append(i)
for i in c:
    d.remove(i)
    if len(d)==0:
        d.append(-1)
    c=max(d)
    b.append(c)
print(*b)