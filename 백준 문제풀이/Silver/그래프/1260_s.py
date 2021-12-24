from collections import deque
def dfs(graph,v,visted):
    visited[v]=True
    print(v+1, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start]=True
    while queue:
        v=queue.popleft()
        print(v+1 , end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

n,m,v = map(int,input().split())
graph=[[] for _ in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    graph[a-1].append(b-1)
    
visited=[ False for _ in range(n)]
print(visited)
print(graph)
dfs(graph,v,visited) 
bfs(graph,v,visited)