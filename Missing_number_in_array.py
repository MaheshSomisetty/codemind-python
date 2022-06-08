a=int(input())
for i in range(a):
    b=int(input())
    c=list(map(int,input().split()))
    e=(b*(b+1))//2
    f=e-sum(c)
    print(f)