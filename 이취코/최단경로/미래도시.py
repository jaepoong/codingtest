INF = int(1e9)
# 노드, 간선
n,m=map(int,input().split())
# Inf로 초기화 플루이드 워셜
graph=[[INF]*(n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

for _ in range(m):
        a,b=map(int,input().split())
        graph[a][b]==1
        graph[b][a]==1
# 거치는 노드, 목적지 노드
x,k=map(int,input().split())

for i in range(1,n+1):
    for j in range(1,n+1):
        for c in range(1,n+1):
            graph[j][c]= min(graph[j][c], graph[j][i]+graph[i][j])

distance=graph[1][k]+graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)