a=int(input())
b=list(map(int,input().split()))[:a]
d=[]
f=0
for i in b:
    c=len(str(i))
    d.append(c)
e=min(d)
for i in b:
    if(len(str(i))==e):
        f+=1
print(f)