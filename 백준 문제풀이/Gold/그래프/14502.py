from collections import deque
from itertools import combinations
import copy
n,m=map(int,input().split())
lab=[list(map(int,input().split())) for _ in range(n)]

dx=[1,0,-1,0]
dy=[0,1,0,-1]

# 주변 전염
def bfs(graph,x,y):
    queue=deque()
    queue.append((x,y))
    
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            dnx=x+dx[i]
            dny=y+dy[i]
            
            if dnx<0 or dnx>=n or dny<0 or dny>=m:
                continue
            
            if graph[dnx][dny]==1:
                continue
            
            if graph[dnx][dny]==0:
                graph[dnx][dny]=2
                queue.append((dnx,dny))
            
    return graph


def infection(graph): # 현재 상태의 그래프 전체 전염 실행.
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j]==2:
                graph=bfs(graph,i,j)
    return graph
    
def num_0(graph): # 현재 그래프 상에서 0의 개수 찾기
    num=0
    for row in graph:
        for column in row:
            if column == 0 :
                num+=1
    return num

field_0=[]

# 새로 설치할 벽 3개를 선택한다.
for i in range(n):
    for j in range(m):
        if lab[i][j]==0:
            field_0.append((i,j))
# 3개의 조합을 만든다.
comb=combinations(field_0,3)

result=[]
for co in comb:
    my_graph=copy.deepcopy(lab)
    for spot in co:
        my_graph[spot[0]][spot[1]]=1
    
    my_graph=infection(my_graph)
    
    result.append(num_0(my_graph))

print(max(result))