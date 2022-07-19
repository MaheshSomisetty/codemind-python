a=int(input())
for i in range(a):
    b,c=map(int,input().split())
    d=list(map(int,input().split()))
    for i in range(c):
        d.insert(0,d[-1])
        d.pop()
    print(*d)