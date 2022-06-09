a=int(input())
b=list(map(int,input().split()))
c=0
b.append(b[0])
b.append(b[1])
for i in range(1,len(b)-1):
    if((b[i-1]%2==0 and b[i+1]%2!=0) or(b[i-1]%2!=0 and b[i+1]%2==0)):
       c+=1
print(c)  