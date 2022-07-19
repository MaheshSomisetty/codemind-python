def prime(n):
    if n==0:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
def pal(n):
    c=n
    b=0
    while(n):
        a=n%10
        b=b*10+a
        n=n//10
    if c==b:
        return 1
    else:
        return 0
a=int(input())
a=a+1
while(True):
    if pal(a) and prime(a):
        break
    a+=1
print(a)