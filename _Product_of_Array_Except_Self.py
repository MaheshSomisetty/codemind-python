a=int(input())
b=list(map(int,input().split()))
d=1
for i in range(a):
    d*=b[i]
for i in range(a):
    print(d//b[i],end=' ')