a=int(input())
c=0
d=1
while(a):
    b=a%10
    c+=b
    d*=b
    a=a//10
if c==d:
    print('Spy Number')
else:
    print('Not Spy Number')