a=int(input())
while(a):
    s=input()
    if(s==s[::-1]):
        if(len(s)%2==0):
            print("YES EVEN")
        else:
            print("YES ODD")
    else:
        print("NO")
    
    