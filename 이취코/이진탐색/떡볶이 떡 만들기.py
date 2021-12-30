n,m=map(int,input().split())
length=list(map(int,input().split()))


result=0
x=0
while True:
    if x>=m:
        break
    for i in range(n):
        if length[i]>=result:
            x+=1
    result+=1
    
print(result)