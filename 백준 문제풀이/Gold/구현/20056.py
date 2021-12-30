# n크기 격자, m개의 파이어볼, k번 실행
n, m, k = map(int,input().split())
fireball=[]
# fireball의 5개의 요소가 들어간다
# r,c,m,d,s = y,x,질량,방향,속력
for i in range(m):
    fireball.append(list(map(int,input().split()))) 

# 방향 벡터
dx=[0,1,1,1,0,-1,-1,-1]
dy=[1,1,0,-1,-1,-1,0,1]

for i in range(k):
    for j in fireball:
        