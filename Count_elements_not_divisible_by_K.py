a,b=map(int,input().split())
c=list(map(int,input().split()))[:a]
d=0
for i in c:
    if(i%b==0):
        d+=1
print(a-d)