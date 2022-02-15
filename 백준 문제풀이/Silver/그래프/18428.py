from itertools import combinations
import copy
n=int(input())
graph=[list(input().split()) for _ in range(n)]

empty=[]
teacher=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]=='X':
            empty.append([i,j])
        if graph[i][j]=='T':
            teacher.append([i,j])

combi=list(combinations(empty,3))

dy=[1,-1,0,0]
dx=[0,0,1,-1]

for comb in combi:
    gra=copy.deepcopy(graph)
    for com in comb:
        gra[com[0]][com[1]]='O'
    
    for tea in teacher:
        for i in range(4):
            gra