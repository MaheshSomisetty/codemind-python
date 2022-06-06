c=0
a=int(input())
for i in range(a):
    b=input()
    if('+' in b):
        c+=1
    else:
        c-=1
print(c)
