a=int(input())
b=str(a)
c=0
for i in b:
    if b.count(i)!=1:
        c=1
        break
if c==0:
    print("Unique Number")
else:
    print("Not Unique Number")
    