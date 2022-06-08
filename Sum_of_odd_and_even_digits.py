a=int(input())
b=list(map(int,input().split()))
c=0
d=0
for i in range(a):
    if(i%2):
        c+=b[i]
for i in range(a):
    if(i%2==0):
        d+=b[i]
if(c-d==0):
    print("YES")
else:
    print("NO")