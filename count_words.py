a=input()
a=a.lower()
a=a.split()
b=0
for i in a:
    if i.startswith('a') or  i.startswith('e') or  i.startswith('i') or  i.startswith('o') or  i.startswith('u'):
        b+=1
print(b)