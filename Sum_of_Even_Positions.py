a=int(input())
b=list(map(int,input().split()))
c=0
for i in range(0,a,2):
    c+=b[i]
print(c)