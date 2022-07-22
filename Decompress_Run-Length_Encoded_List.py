a=int(input())
b=list(map(int,input().split()))
c=[]
d=[]
for i in range(0,a,2):
    for j in range(b[i]):
        c.append(b[i+1])    
print(*c)