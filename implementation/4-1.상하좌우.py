n=int(input())
x=list(input().split())
result=[1,1]
for i in x:
    if i=='R' and result[0]<n:
        result[0]+=1
    elif i=='L' and result[0]>1:
        result[0]-=1
    elif i=='D' and result[1]<n:
        result[1]+=1
    elif i=='U' and result[1]>1:
        result[1]-=1
print(f'{result[0]} {result[1]}')
