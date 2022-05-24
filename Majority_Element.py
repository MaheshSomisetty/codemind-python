a=int(input())
b=list(map(int,input().split()))[:a]
c=[]
for i in b:
    d=b.count(i)
    c.append(d)
f=max(c)
for i in b:
    if b.count(i)==f:
        print(i)
        break