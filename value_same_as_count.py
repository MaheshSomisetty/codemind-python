a=int(input())
c=0
d=[]
b=list(map(int,input().split()))[:a]
for i in b:
    if(i==b.count(i)):
        d.append(i)
d=set(d)
print(len(d))