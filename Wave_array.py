n=int(input())
b=list(map(int,input().split()))
c=0
for i in range(n-2):
    if((b[i]>b[i+1]) and (b[i+1]<b[i+2])) or ((b[i]<b[i+1]) and (b[i+1]>b[i+2])):
        pass
    else:
        c=1
        break
if(c==1):
    print("no")
else:
    print('yes')