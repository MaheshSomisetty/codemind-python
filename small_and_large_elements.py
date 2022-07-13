a=input()
a=a.split()
d=len(a)-1
b=a[0]
c=a[d]
e=[]
f=[]
for i in b:
    e.append(ord(i))
for i in c:
    f.append(ord(i))
g=min(e)
h=max(f)
print(chr(g),chr(h))

