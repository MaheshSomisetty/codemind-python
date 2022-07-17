a=input()
a=a.split()
c=[]
for i in a:
    c.append(len(i))
print(min(c))