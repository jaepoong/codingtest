from itertools import combinations
n , m = map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]

def chicken_dis(h,d):
    d1=abs(h[0]-d[0])
    d2=abs(h[1]-d[1])
    return d1+d2

home=[]
chicken=[]
# 집 치킨 구분
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            home.append([i,j])
            continue
        if graph[i][j]==2:
            chicken.append([i,j])

combination = list(combinations(chicken,m))

result=[]
for combi in combination:
    chicks=[]
    for h in home:
        mini=[]
        for chick in combi:
            mini.append(chicken_dis(chick,h))
        chicks.append(min(mini))
    result.append(sum(chicks))

print(min(result))
123