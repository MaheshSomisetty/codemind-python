a=int(input())
b=list(map(int,input().split()))[:a]
d=[]
for i in b:
    c=len(str(i))
    d.append(c)
e=max(d)
for i in b:
    if(len(str(i))==e):
        print(i,end=" ")