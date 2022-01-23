n,k=map(int,input().split())
graph=[[1]*n for i in range(k)]
for i in range(k):
    graph[i][0]=i+1

for i in range(1,k):
    for j in range(1,n):
        graph[i][j]=graph[i-1][j]+graph[i][j-1]

print(graph[k-1][n-1]%1000000000)