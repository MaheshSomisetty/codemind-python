a=input()
a=a.lower()
b=set(a)
b=list(b)
d=[]
e=[]
for i in b:
    if i==' ':
        b.remove(' ')
for i in b:
    if a.count(i)==1:
        d.append(i)
for i in d:
    e.append(ord(i))
e.sort()
for i in e:
    print(chr(i),end='')