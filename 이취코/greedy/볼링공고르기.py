m,n=map(int,input().split())
li=list(map(int,input().split()))
result=0
for i in range(m):
    for j in range(i+1,m):
        if li[i] != li[j]:
            result+=1

print(result)