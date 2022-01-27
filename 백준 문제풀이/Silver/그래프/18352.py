from collections import deque
import sys
input = sys.stdin.readline
n,m,k,x=map(int,input().split())
graph=[[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)

queue=deque()

distance=[-1]*(n+1)
distance[x]=0
queue.append(x)

while queue:
    now=queue.popleft()
    for i in graph[now]:
        if distance[i]==-1:
            distance[i]=distance[now]+1
            queue.append(i)

r=False
for i in range(1,n+1):
    if distance[i]==k:
        print(i)
        r=True

if not r:
    print(-1)