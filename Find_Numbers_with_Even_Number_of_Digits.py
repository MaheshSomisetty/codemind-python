def count(n):
    c=0
    while(n):
        n=n//10
        c=c+1
    return c

        
n=int(input())
b=list(map(int,input().split()))[:n]
d=0
for i in b:
    if(count(i)%2==0):
        d=d+1
print(d)
