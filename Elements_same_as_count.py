a=int(input())
b=list(map(int,input().split()))
c=[]
d=0
for i in b:
    if i not in c:
        c.append(i)
for i in c:
    if b.count(i)==i:
        print(i,end=' ')
        d=1
if d==0:
    print(-1)