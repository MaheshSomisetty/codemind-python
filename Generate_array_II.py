a=int(input())
b=list(map(int,input().split()))
c=[]
for i in range(0,a,2):
    for j in range(b[i+1]):
        c.append(b[i])
print(*c)