a=int(input())
b=list(map(int,input().split()))
c=[]
e=[]
for i in b:
    if i not in e:
        e.append(i)
for i in e:
    print(i,b.count(i),end=' ')