a=int(input())
b=list(map(int,input().split()))
c,d=map(int,input().split())
e=[]
for i in range(a):
    if b[i]>=c and b[i]<=d:
        e.append(b[i])
if e==[]:
    print(-1)
else:
    print(max(e))