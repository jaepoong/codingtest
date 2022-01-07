from collections import deque
m,n,k=map(int,input().split()) # M=높이, N=너비, k=직사각형 개수
square=[list(map(int,input().split())) for _ in range(k)]

graph=[[0]*n for _ in range(m)]
for squ in square:
    for i in range(squ[0],squ[2]): # x값
        for j in range(squ[1],squ[3]): # y값
            graph[j][i]==-1
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
            if 0<=dnx<n and 0<=dny<m and graph[dny][dnx] != -1 and graph[dny][dnx] == 0:
                graph[dny][dnx]==1
                queue.append((dnx,dny))

result=0

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            bfs(i,j)
            result+=1

print(result)