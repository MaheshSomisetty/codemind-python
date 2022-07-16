a=input()
a=a.lower()
a=set(a)
a=list(a)
for i in a:
    if i==' ':
        a.remove(' ')
b=[]
for i in a:
    b.append(ord(i))
b.sort()
c=''
for i in b:
    c+=chr(i)
print(c)