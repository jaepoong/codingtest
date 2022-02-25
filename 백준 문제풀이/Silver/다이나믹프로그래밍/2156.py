n=int(input())
graph=[]
for i in range(n):
    graph.append(int(input()))

dp=[[0] for i in range(n)]
dp[0]=graph[0]
dp[1]=graph[0]+graph[1]
dp[2]=max(dp[0]+graph[2],graph[1]+graph[2])
for i in range(3,n):
    dp[i]=max(dp[i-1],dp[i-2]+graph[i],dp[i-3]+graph[i-1]+graph[i])

print(dp[n-1])