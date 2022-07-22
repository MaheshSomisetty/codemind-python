a,b=map(int,input().split())
c=list(map(int,input().split()))
d=0
e=0
for i in c:
    if i<=b:
        d+=1
    else:
        e+=1
    if e>1:
        break
print(d)