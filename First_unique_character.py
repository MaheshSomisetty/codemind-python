a=input()
a=a.lower()
b=[]
for i in a:
    if a.count(i)==1:
        b.append(i)
        break
if b==[]:
    print(-1)
else:
    print(*b)