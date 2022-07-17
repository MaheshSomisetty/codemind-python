a=input()
a=a.lower()
a=a.split()
b=input()
b=b.lower()
b=b.split()
c=[]
for i in b:
    if i in a:
        c.append(i)
print(len(c))