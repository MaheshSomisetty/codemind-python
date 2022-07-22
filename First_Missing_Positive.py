a=int(input())
b=list(map(int,input().split()))
for i in range(1,max(b)+2):
    if i not in b:
        print(i)
        break