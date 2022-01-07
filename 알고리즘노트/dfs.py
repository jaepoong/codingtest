from collections import deque
n,m=map(int,input().split())
graph=[]
def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=m:
        return False
    
    if graph[x][y]==0:
        graph[x][y]=1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

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
            if dnx<0 or dnx>=n or dny<0 or dny>=m:
                continue
            if graph[dny][dnx]==1:
                graph[dny][dnx]=graph[dy][dx]+1
                queue.append((dnx,dny))
    return graph[n-1][m-1]

