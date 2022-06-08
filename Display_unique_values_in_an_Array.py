a=int(input())
b=list(map(int,input().split()))
c=[]
d=0
for i in b:
    if(b.count(i)==1):
        c.append(i)
        d=1
if(d==1):
    print(*c)
else:
    print(-1)
    