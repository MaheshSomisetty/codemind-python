a=int(input())
b=list(map(int,input().split()))
c=[]
for i in b:
    if i**0.5==int(i**0.5):
        c.append(i)
print(sum(c))