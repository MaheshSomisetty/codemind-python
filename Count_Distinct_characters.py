a=input()
a=a.lower()
a=set(a)
a=list(a)
for i in a:
    if i==' ':
        a.remove(' ')
print(len(a))