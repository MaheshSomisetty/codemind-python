a=input()
c=a.lower()
b=c.split()
c=0
for i in b:
    d=i
    if(d==d[::-1]):
        c=c+1
print(c)
