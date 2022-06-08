a=int(input())
b=list(map(int,input().split()))
c=0
for i in b:
    if(i%2):
        c+=1
if(c<=2):
    print("YES")
else:
    print("NO")