a=int(input())
b=int(input())
c=0
for i in range(a):
    c+=sum(list(map(int,input().split())))
print(c)