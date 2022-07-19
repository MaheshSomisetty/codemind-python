a=int(input())
b=a*a 
b=str(b)
x=b[::-1]
f=str(a)
c=int(f[::-1])
d=c*c 
if x==str(d):
    print("True")
else:
    print("False")