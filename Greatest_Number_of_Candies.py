a=int(input())
b=list(map(int,input().split()))
c=int(input())
for i in b:
    if i+c>=max(b):
        print(True,end=' ')
    else:
        print(False,end=' ')