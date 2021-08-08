n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))
def ice(x,y):
    if x<0 or x>=m or y<0 or y>=n:
        return False
    if graph[x][y]==0:
        graph[x][y]=1
        ice(x-1,y)
        ice(x+1,y)
        ice(x,y-1)
        ice(x,y+1)
        return True
    return False
result=0
for i in range(n):
    for j in range(m):
        if ice(i,j)==True:
            result+=1
print(result)
