from collections import deque
n,l,r=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]
dy=[1,-1,0,0]
dx=[0,0,1,-1]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            dny=y+dy[i]
            dnx=x+dx[i]
            
            if 0<=dny<n and 0<=dnx<n :
                if l<=abs(graph[y][x]-graph[dny][dnx])<=r and not visited[dny][dnx]:
                    gra[dny][dnx]=num
                    visited[dny][dnx]=True
                    queue.append([dnx,dny])
                

while True:
    visited=[[False]*n for _ in range(n)]
    gra=[[0]*n for _  in range(n)]
    num=0
    for i in range(n):
        for j in range(n):
            if visited[i][j]==False:
                num+=1
                bfs(j,i)
    print(gra)
    if num==0:
        break
    
                