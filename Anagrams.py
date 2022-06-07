a=input()
b=input()
c=a.lower()
d=b.lower()
e=[]
f=[]
for i in c:
    e.append(ord(i))
e.sort()
for i in d:
    f.append(ord(i))
f.sort()
if e==f:
    print("True")
else:
    print("False")