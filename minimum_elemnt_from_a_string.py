a=input()
a=a.split()
b=sorted(a[-1])
c=b[0]
if c.lower() in b:
    print(c.lower())
else:
    print(c)