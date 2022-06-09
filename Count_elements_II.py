a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
e=set(c)
f=set(d)
g=0
for i in e:
    if i not in f:
        g+=1
for i in f:
    if i not in e:
        g+=1
print(g)