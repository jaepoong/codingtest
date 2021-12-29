import sys
m,n=map(int,sys.stdin.readline().split())
graph=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dx=[1,-1,0,0]
dy=[0,0,-1,1]
result=0
while True:
    condition=0
    for i in range(n):#행
        for j in range(m):#열
            if graph[i][j]==0 or graph[i][j]==-1:
                continue
            
            if graph[i][j]==result+1:
                for k in range(4):
                    dny=i+dy[k]
                    dnx=j+dx[k]
                    
                    if dnx<0 or dnx>=m or dny<0 or dny>=n:
                        continue
                    
                    if graph[dny][dnx]==0:
                        graph[dny][dnx]=graph[i][j]+1
                        condition+=1

    if condition==0:
        break
    result+=1

my=0
for i in graph:
    if 0 in i:
        my+=1

if my:
    print(-1)        
else:
    print(result)
