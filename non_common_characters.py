a=input()
b=input()
a=a.lower()
a=a.replace(" ", "")
a=list(a)
b=b.lower()
b=b.replace(" ", "")
b=list(b)
c=[]
x=""
y=""
for i in a:
    if i not in x:
        x=x+i
for i in b:
    if i not in y:
        y=y+i
for i in x:
    if i not in y:
        c.append(i)
for i in y:
    if i not in x:
        c.append(i)
c=sorted(c)
for i in c:
    print(i,end="")
