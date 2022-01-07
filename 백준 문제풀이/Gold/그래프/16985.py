from collections import deque

graph=[]

for i in range(5):
    grap=[list(map(int,input().split())) for _ in range(5)]
    graph.append(grap)

def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret

graph_list=[[]]*5
for i in range(5):
    g=graph[i]
    for j in range(4):
        g=rotate_90(g)
        if i==0 and g[0][0]==1:
            continue
        if i==4 and g[4][4]==1:
            continue
        graph_list[i].append(g)
        

dx=[1,-1,0,0,0,0]
dy=[0,0,1,-1,0,0]
dz=[0,0,0,0,1,-1]



def bfs(x,y,z,graph):
    queue=deque()
    queue.append((x,y,z))
    while queue:
        x,y,z=queue.popleft()
        for i in range(6):
            dnx=x+dx[i]
            dny=y+dy[i]
            dnz=z+dz[i]
            if 0<dnx or 5>=dnx or 0<dny or 5>= dny or 0 < dnz or 5 >= dnz:
                continue
            if graph[dnz][dny][dnx]==1:
                continue
            queue.append((dnx,dny,dnz))
            graph[dnz][dny][dnx]+=graph[z][y][x]
    if graph[4][4][4] == 0 or graph[4][4][4]==1:
        return False
    else:
        return graph[4][4][4]*(-1)
    
#bfs(0,0,0)
print(graph_list[0])
#print(graph[4][4][4]*(-1))