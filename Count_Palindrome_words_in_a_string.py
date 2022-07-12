a=input()
a=a.lower()
a=a.split()
b=0
for i in a:
    if i==i[::-1]:
        b+=1
print(b)