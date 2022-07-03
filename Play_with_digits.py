a=int(input())
b=list(map(int,input().split()))
c=0
for i in b:
    while(i):
        d=i%10
        c+=d
        i=i//10
print(c)