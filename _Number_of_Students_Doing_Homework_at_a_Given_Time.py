a=int(input())
b=list(map(int,input().split()))
c=int(input())
d=list(map(int,input().split()))
e=int(input())
f=0
for i in range(a):
    if e>=b[i] and e<=d[i]:
        f+=1
print(f)