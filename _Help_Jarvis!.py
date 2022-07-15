a=int(input())
for i in range(a):
    c=input()
    b=[]
    for i in c:
        b.append(int(i))
    if min(b)+3==max(b):
        print("YES")
    else:
        print("NO")