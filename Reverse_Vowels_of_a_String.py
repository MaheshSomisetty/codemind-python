a=input()
a=list(a)
d=[]
for i in a:
    d.append(i)
b=[]
c=[]
for i in range(len(a)):
    if a[i] in 'aeiouAEIOU':
        b.append(a[i])
        c.append(i)
        d.remove(a[i])
b=b[::-1]
for i in range(len(b)):
    d.insert(c[i],b[i])
for i in d:
    print(i,end='')