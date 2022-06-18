a=int(input())
b=list(map(int,input().split()))
c=0
d=0
for i in b:
    if i%2:
        c+=i
    else:
        d+=i
print(abs(c-d))