a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
e=[]
for i in c:
    if i not in d:
        e.append(i)
for i in d:
    if i not in c:
        e.append(i)
print(*e)
