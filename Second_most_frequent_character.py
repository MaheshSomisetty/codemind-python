a=input()
b=[]
for i in a:
    b.append(a.count(i))
c=max(b)
for i in a:
    if a.count(i)==c:
        a=a.replace(i,"")
e=[]
for i in a:
    e.append(a.count(i))
if e==[]:
    print(-1)
else:
    c=max(e)
    for i in a:
        if a.count(i)==c:
            print(i)
            break
    

