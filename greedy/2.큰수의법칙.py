n,m,k=map(int,input().split())
data=list(map(int,input().split()))
data.sort()
max=data[n-1]
max2=data[n-2]
x=0
result=0
for i in range(m):
    if x<k:
        result+=max
    else:
        result+=max2
        x=0
    x+=1
print(result)
