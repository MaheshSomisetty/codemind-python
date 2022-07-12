a=input()
b=input()
a=a.lower()
b=b.lower()
a=a.split()
b=b.split()
e=set(a)
f=set(b)
c=e.intersection(f)
e=list(a)
f=list(b)
d=0
for i in c:
    if a.count(i)==1 and b.count(i)==1:
        d+=1
print(d)