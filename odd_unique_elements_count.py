a=int(input())
d=list(map(int,input().split()))[:a]
c=0
b=set(d)
for i in b:
    if(i%2):
        c+=1
print(c)