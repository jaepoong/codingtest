from collections import deque
def solution(n, computers):
    def bfs(com):
        visited[com]=True
        queue=deque()
        queue.append(com)
        while queue:
            com=queue.popleft()
            visited[com]=True
            for i in range(n):
                if i !=com and computers[com][i]==1:
                    if visited[i]==False:
                        queue.append(i)
    
    visited = [False for _ in range(n)]
    answer=0
    for com in range(n):
        if visited[com]==False:
            bfs(com)
            answer+=1
    return answer