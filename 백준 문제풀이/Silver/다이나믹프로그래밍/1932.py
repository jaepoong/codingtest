n=int(input())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))

t=2

for i in range(1,n):
    for j in range(t):
        if j==0:
            graph[i][j]=graph[i-1][j]+graph[i][j]
        elif j==i:
            graph[i][j]=graph[i-1][j-1]+graph[i][j]
        else:
            graph[i][j]=max(graph[i-1][j-1]+graph[i][j],graph[i-1][j]+graph[i][j])
    t+=1
print(max(graph[n-1]))