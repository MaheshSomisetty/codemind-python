a=int(input())
b=list(map(int,input().split()))
if a<3:
    print(max(b))
else:
    b=set(b)
    b=list(b)
    b.sort()
    print(b[-3])