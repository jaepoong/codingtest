m,n=map(int,input().split())
growing=[list(map(int,input().split())) for j in range(m)]

graph=[[1]*m]*m

for i in range(n):
    grow=[0*m]*m
    for j in 