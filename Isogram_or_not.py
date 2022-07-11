a=input()
b=0
for i in a:
    if a.count(i)==1:
        b+=1
if b==len(a):
    print(True)
else:
    print(False)