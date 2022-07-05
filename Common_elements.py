a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
e=[]
f=[]
for i in c:
    if i not in e:
        e.append(i)
for i in e:
    if i in d:
        f.append(i)
print(*f)
        