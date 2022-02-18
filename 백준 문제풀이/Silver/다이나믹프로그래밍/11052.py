n=int(input())
card=list(map(int,input().split()))
li=[[0 for _ in range(n)] for i in range(n)]
for i in range(n):
    li[i]=card[0]*i

for i in range(1,n):
    for j in range(i,n):
        li[i][j]=max(li[i-1][j],li[i-1][j-i]+card[i])

result=[]
for i in range(n):
    result.append(li[i][n-1])

print(max(result))