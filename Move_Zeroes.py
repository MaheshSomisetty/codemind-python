a=int(input())
b=list(map(int,input().split()))
for i in b:
    if i==0:
        b.remove(0)
        b.append(0)
print(*b)