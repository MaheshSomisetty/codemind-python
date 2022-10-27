s=input()
v=''
for i in s:
    if i>='a' and i<='z':
        v+=i
v=v[::-1]
ans=''
k=0
for i in s:
    if i in v:
        ans+=v[k]
        k+=1
        continue
    ans+=i
print(ans)