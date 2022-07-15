a=int(input())
for i in range(a):
    b=int(input())
    c=list(map(int,input().split()))
    for i in range(b):
        if sum(c[0:i])==sum(c[i+1:]):
            print("YES")
            break
    else:
        print("NO")