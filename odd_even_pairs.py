a=int(input())
b=list(map(int,input().split()))
c=[]
d=[]
e=[]
for i in b:
    if i%2==0:
        c.append(i)
    else:
        d.append(i)
f=len(c)
g=len(d)
h=min(f,g)
j=max(f,g)-h
for i in range(h):
    e.append(d[i])
    e.append(c[i])
for i in range(j):
    if(f>g):
        e.append(c[h+i])
    else:
        e.append(d[h+i])
if(len(e)%2!=0):
    e.append(0)
print(*e)
    