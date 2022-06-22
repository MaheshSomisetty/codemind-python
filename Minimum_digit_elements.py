a=int(input())
b=list(map(int,input().split()))
c=min(b)
d=(len(str(c)))
e=0
for i in b:
    if(len(str(i))==d):
        e+=1
print(e)