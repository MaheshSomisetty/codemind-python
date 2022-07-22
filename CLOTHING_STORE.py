a=int(input())
b=list(map(int,input().split()))
c=set(b)
d=[]
e=[]
for i in c:
    d.append(b.count(i))
for i in d:
    e.append(int(i/2))
print(sum(e))