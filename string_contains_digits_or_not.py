a=int(input())
while(a>=0):
    b=input()
    c=0
    for i in b:  
        if(i.isdigit()):
             c+=1
    if(c>0):
        print('Yes')
    else:
        print('No')
    a-=1