a=int(input())
b=list(map(int,input().split()))
c=[]
d=0
for i in b:
    if i==1:
        d+=1
    c.append(d)
    if i==0:
        d=0
print(max(c))