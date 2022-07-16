a=int(input())
b=0
while(a):
    c=a%10
    b+=c
    a=a//10
    if a==0 and b>9:
        a=b
        b=0
print(b)