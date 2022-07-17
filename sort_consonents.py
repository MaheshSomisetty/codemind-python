a=input()
a=a.split()
for i in a:
    c=[]
    d=[]
    f=[]
    g=''
    for j in range(len(i)):
        if i[j] not in "aeiouAEIOU":
            c.append(i[j])
        if i[j] in "aeiouAEIOU":
            d.append(j)
            f.append(i[j])
    e=sorted(c)
    for j in range(len(d)):
        e.insert(d[j],f[j])
    for i in e:
        g+=i
    print(g,end=" ")
        