a=input()
b=a.lower()
c=0
for i in b:
    if(i.isalpha()):
        continue
    elif i.isdigit():
        continue
    elif i==' ':
        continue
    else:
        c+=1
print(c)