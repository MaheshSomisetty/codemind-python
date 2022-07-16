n=int(input())
res=0
x=n
if n<0:
    n=-n
while n:
    d=n%10
    res=res*10+d
    n=n//10
if x>0:
    print(res)
else:
    print(-res)