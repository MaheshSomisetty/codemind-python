def pal(n):
    b=0
    c=n
    while(n):
        a=n%10
        b=b*10+a
        n=n//10
    return b
    
a=int(input())
b=list(map(int,input().split()))
c=0
for i in range(a):
    print(pal(b[i]),end=' ')