a=input()
b=0
for i in a:
    if i in '1234567890':
        b+=1
if b==0:
    print('Doesn't contain digit')
else:
    print('Contains',b,'digit')