a=int(input())
b=list(map(int,input().split()))
c=0
d=0
for i in range(0,a,2):
    c+=b[i]
for i in range(1,a,2):
    d+=b[i]
print(c-d)
    