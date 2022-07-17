a,b=map(int,input().split())
c=list(map(int,input().split()))
d=0
for i in c:
    if len(str(abs(i)))==b:
        d+=1
print(d)