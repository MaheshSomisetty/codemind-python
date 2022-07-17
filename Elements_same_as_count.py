a=int(input())
b=list(map(int,input().split()))
c=[]
e=[]
for i in b:
    if i not in e and b.count(i)>1:
        e.append(i)
for i in e:
    if b.count(i)==i:
        c.append(i)
if c==[]:
    print(-1)
else:
    print(*c)
    