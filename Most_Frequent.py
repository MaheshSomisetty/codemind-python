a=int(input())
b=list(map(int,input().split()))
c=set(b)
c=list(c)
d=[]
for i in c:
    d.append(b.count(i))
f=max(d)
e=d.index(f)
print(c[e])