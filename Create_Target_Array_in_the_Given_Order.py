a=int(input())
b=list(map(int,input().split()))
c=int(input())
d=list(map(int,input().split()))
e=[]
for i in range(a):
    e.insert(d[i],b[i])
print(*e)