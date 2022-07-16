a=input()
a=a.lower()
b=[]
c=''
for i in a:
    if a.count(i)==1:
        b.append(i)
for i in b:
    if i==' ':
        b.remove(' ')
b.sort()
for i in b:
    c+=i
print(c)