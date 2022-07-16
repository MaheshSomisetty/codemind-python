a=input()
a=a.lower()
b=input()
b=b.lower()
c=[]
for i in a:
    if i in b:
        c.append(i)
c=set(c)
c=list(c)
for i in c:
    if i==' ':
        c.remove(' ')
print(len(c))