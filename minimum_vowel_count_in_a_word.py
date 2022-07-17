a=input()
a=a.lower()
a=a.split()
c=[]
for i in a:
    b=0
    for j in i:
        if j in 'aeiou':
            b+=1
    c.append(b)
print(min(c))