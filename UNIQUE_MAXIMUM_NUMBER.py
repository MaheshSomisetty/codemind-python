a=int(input())
b=list(map(int,input().split()))
c=[]
for i in b:
    if b.count(i)==1:
        c.append(i)
if c==[]:
    print(-1)
else:
    print(max(c))