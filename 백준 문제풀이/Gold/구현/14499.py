# 세로,가로,x위치,y위치 주사위, 명령 개수
n,m,x,y,k=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]
# 1,2,3,4 : 동,서,북,남
order=list(map(int,input().split()))
dice=[[0,2,0],[4,1,3],[0,5,0],[0,6,0]]
graph[y][x]=6

def dice_change(order):
    if order==1:
        dice[1][0],dice[1][1],dice[1][2],dice[3][1] = dice[3][1],dice[1][0],dice[1][1],dice[1][2]
        return dice[3][1]
    if order==2:
        dice[1][0],dice[1][1],dice[1][2],dice[3][1] = dice[1][1],dice[1][2],dice[3][1],dice[1][0]
        return dice[3][1]
    if order==3:
        dice[0][1],dice[1][1],dice[2][1],dice[3][1] = dice[1][1],dice[2][1],dice[3][1],dice[0][1]
        return dice[3][1]
    if order==4:
        dice[0][1],dice[1][1],dice[2][1],dice[3][1] = dice[3][1],dice[0][1],dice[1][1],dice[2][1]
        return dice[3][1]
dx=[1,-1,0,0]
dy=[0,0,1,-1]

def dice_move(x,y,order):
    dnx=x+dx[order-1]
    dny=y+dy[order-1]
    if dnx<0 or dnx>=m or dny< 0 or dny >=n:
        return dnx,dny,False
    dice_change(order)
    
    if graph[dny][dnx]==0:
        graph[dny][dnx]=dice[3][1]
    else:
        dice[3][1]=graph[dny][dnx]
        graph[dny][dnx]=0
    return dnx,dny,True

for i in  order:
    dnx,dny,va=dice_move(x,y,i)
    if va:
        x,y=dnx,dny
        print(dice[1][1])