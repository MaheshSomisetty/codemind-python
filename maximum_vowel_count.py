a=input()
a=a.split()
b=[]
for i in a:
    c=0
    for j in i:
        if j in 'aeiou':
            c+=1
            b.append(c)
print(max(b))