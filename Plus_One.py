a=int(input())
b=list(map(int,input().split()))
c=''
for i in b:
    c+=str(i)
c=int(c)
c=c+1
c=str(c)
for i in c:
    print(i,end=' ')