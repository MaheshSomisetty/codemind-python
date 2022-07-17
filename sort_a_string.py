a=input()
a=list(a)
c=[]
d=[]
f=""
for i in range(len(a)):
    if a[i] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789":
        c.append(a[i])
        d.append(i)
s=''.join(filter(str.isalnum,a))

s=sorted(s)
for i in range(len(c)):
    s.insert(d[i],c[i])
z="".join(s)
print(z)
  