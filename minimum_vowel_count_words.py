a=input()
a=a.lower()
a=a.split()
c=[]
for i in a:
    d=0
    for j in i:
        if j in 'aeiou':
            d+=1
    c.append(d)
e=min(c)
print(c.count(e))
    