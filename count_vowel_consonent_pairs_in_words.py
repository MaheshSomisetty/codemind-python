a=input()
a=a.split()
f=0
for i in a:
    i=list(i)
    if len(i)%2==0:
        b=len(i)/2
    else:
        b=len(i)//2
    c=[]
    d=[]
    for j in range(int(b)):
        c.append(i[j])
        d.append(i[len(i)-j-1])
    for i in range(len(c)):
        if c[i] in "AEIOUaeiou" and d[i] not in "AEIOUaeiou":
            f=f+1
        if c[i] not in "AEIOUaeiou" and d[i] in "AEIOUaeiou":
            f=f+1
print(f)