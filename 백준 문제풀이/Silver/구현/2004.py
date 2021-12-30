n,m=map(int,input().split())

p=1
for i in range(n,n-m,-1):
    p=p*i
p=list(str(p))
x=list(reversed(p))
result=0
for i in x:
    if i!='0':
        break
    result+=1
print(result)