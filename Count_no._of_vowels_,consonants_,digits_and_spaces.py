a=input()
b=0
c=0
d=0
e=0
for i in a:
    if(i in 'AEIOUaeiou'):
        b+=1
    elif(i>='A' and i<='Z') or (i>='a' and i<='z'):
        c+=1
    elif(i.isdigit()):
        d+=1
    elif(i==' '):
        e+=1
print('Vowels:',b)
print('Consonants:',c)
print('Digits:',d)
print('White spaces:',e)
        