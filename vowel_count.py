a=input()
b=a.lower()
c=0
for i in b:
    if i in 'aeiou':
        c+=1
print(c)