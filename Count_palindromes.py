def pal(n):
    b=0
    c=n
    while(n):
        a=n%10
        b=b*10+a
        n=n//10
    if(c==b):
        return 1
    else:
        return 0
    
a=int(input())
b=list(map(int,input().split()))
c=0
for i in range(a):
    if(pal(b[i])):
         c+=1
print(c)