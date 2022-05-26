def prime(n):
    e=0  
    for i in range(1,n+1):
        if n%i==0:
          e+=1
    if(e==2):
         return 1
    else:
        return 0
a=int(input())
b=list(map(int,input().split()))[:a]
d=0
for i in range(a):
    if(prime(b[i])):
        d+=1
    
print(d)
        