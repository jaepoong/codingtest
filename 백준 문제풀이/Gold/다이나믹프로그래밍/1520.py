import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

m,n =map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(m)]

dx=[1,-1,0,0]
dy=[0,0,1,-1]

destination=[m-1,n-1]
x=0

def dfs(v):
    global x
    if v==destination:
        x+=1
        return 
    
    for i in range(4):
        dnx=v[1]+dx[i]
        dny=v[0]+dy[i]
        
        if dnx<0 or dnx>=n or dny<0 or dny>=m:
            continue
        if graph[dny][dnx]<graph[v[0]][v[1]]:
            dfs([dny,dnx])

dfs([0,0])
print(x)
