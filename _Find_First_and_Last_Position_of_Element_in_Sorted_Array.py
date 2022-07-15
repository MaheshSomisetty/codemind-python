a=int(input())
b=list(map(int,input().split()))
c=int(input())
d=[]
for i in range(a):
    if b[i]==c:
        d.append(i)
if d==[]:
    print(-1,-1)
else:
    print(min(d),max(d))

        