a,b=map(int,input().split())
c=list(map(int,input().split()))
d=[]
for i in range(b):
    c.append(c[0])
    c.remove(c[0])
print(*c)