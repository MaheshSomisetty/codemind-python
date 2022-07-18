a=input()
f=0
c=[]
d=[]
if len(a)%2==0:
    b=len(a)/2
else:
    b=len(a)//2
for i in range(int(b)):
    c.append(a[i])
    d.append(a[len(a)-i-1])
for i in range(len(c)):
    if c[i] in "AEIOUaeiou" and d[i] in "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz":
        f=f+1
    if c[i] in "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz" and d[i] in "AEIOUaeiou":
        f=f+1
print(f)