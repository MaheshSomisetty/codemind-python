a=int(input())
b=list(map(int,input().split()))
d=[]
for i in range(a):
    c=0
    for j in range(a):
        if(b[i]>b[j]):
            c+=1
    d.append(c)
print(*d)