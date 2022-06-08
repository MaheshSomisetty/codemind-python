a=int(input())
c=[]
d=0
while(a):
    b=a%10
    a=a//10
    c.append(b)
for i in c:
    if(c.count(i)==1):
        d+=1
if(d==len(c)):
    print('Unique Number')
else:
    print('Not Unique Number')
        