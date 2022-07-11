a=input()
a=a.split()
b=[]
for i in range(len(a)):
    b.append(len(a[i]))
print(min(b))