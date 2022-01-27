from collections import deque
n=int(input())
dy=[1,-1,0,0]
dx=[0,0,-1,1]
def find_fire(graph):
    fire=[]
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j]=='*':
                fire.append([i,j])
    return fire

def find_sangeun(graph):
    sangeun=[]
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j]=='@':
                sangeun.append([i,j])
    return sangeun

def is_out(graph):
    if "@" in graph[0] or "@" in graph[len(graph)]:
        return True
    for i in range(1,len(graph)-1):
        if graph[i][0] == "@" or graph[i][len(graph[0])] =="@":
            return True
    return False

for _ in range(n):
    w,h=map(int,input().split())
    graph=[]
    for _ in range(h):
        graph.append(list(input().strip()))
    time=0
    while True:
        time+=1
        # 불붙이기
        move=0
        for fi in find_fire(graph):
            for i in range(4):
                dny=fi[0]+dy[i]
                dnx=fi[1]+dx[i]
                if 0<=dny<h and 0<=dnx<w and graph[dny][dnx]=='.':
                    graph[dny][dnx]='*'
        #상근이 이동
        for sangeun in find_sangeun(graph):
            for i in range(4):
                dny=sangeun[0]+dy[i]
                dnx=sangeun[0]+dx[i]
                if 0<=dny<h and 0<=dnx<w and graph[dny][dnx]=='.':
                    graph[dny][dnx]='@'
                    move+=1
        
        if move:
            print("IMPOSSIBLE")
        
        if is_out(graph):
            print(time)
        
        
            
        