from collections import deque
row,column=map(int,input().split())

graph=[list(map(int,input().split())) for _ in range(row)]

dx = [-1, -1, -1, 0, 1, 0, 1, 1]
dy = [-1, 0, 1, 1, 1, -1, 0, -1]
queue=deque()
for i in range(row):
    for j in range(column):
        if graph[i][j]==1:
            queue.append((i,j))

while queue:
    x,y=queue.popleft()
    for i in range(8):
        dnx=x+dx[i]
        dny=y+dy[i]
        if dnx<0 or dnx>=column or dny<0 or dny>=row:
            continue
        
        if graph[dny][dnx]==0:
            queue.append((dnx,dny))
            graph[dny][dnx]=graph[y][x]+1
result=[]
for i in graph:
    for j in i:
        result.append(j)
print(max(result))