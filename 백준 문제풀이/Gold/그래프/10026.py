from collections import deque
n=int(input())
graph=[list(map(str,input().split())) for _ in range(n)]

dx=[1,-1,0,0]
dy=[0,0,1,-1] 

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            dnx=x+dx[i]
            dny=y+dy[i]
        
            if 0<=dnx<n and 0<=dny<n:
                if graph[dny][dnx]==graph[y][x] and visited[dny][dnx]==0:
                    queue.append((dnx,dny))
                    visited[dny][dnx]=1

visited=[[0]*n for _ in range(n)]
result=0

for i in range(n):
    for j in range(n):
        if visited[i][j]==0:
            bfs(i,j)
            result+=1

print(result)
visited=[[0]*n for _ in range(n)]
result=0

for i in range(n):
    for j in range(n):
        if graph[i][j]=='G':
            graph[i][j]='R'

for i in range(n):
    for j in range(n):
        if visited[i][j]==0:
            bfs(i,j)
            result+=1

print(result)