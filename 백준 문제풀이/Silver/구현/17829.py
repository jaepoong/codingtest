n=map(int(input()))
graph=[list(map(int,input().split())) for _ in range(n)]
def second_pooling(s,d):
    li=[]
    for i in range(s,d):
        for j in range(s,d):
            li.append(graph[i][j])
    li.sort()
    return li[-2]

def(s,d):
    if d-s==1:
        
    