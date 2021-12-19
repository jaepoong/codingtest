n,m=map(int,input().split()) # n 행, m 열
x,y,direction=map(int,input().split())
x=x-1
y=y-1
field=[list(map(int,input().split())) for _ in range(n)]
visit=[[0]*m for _ in range(n)]
visit[x][y]=1

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def rotate():
    global direction
    direction -=1
    if direction==-1:
        direction=3

def go(x,y,direction):
    x_im=x+dx[direction]
    y_im=y+dx[direction]
    if x_im<0 or x_im >=m or y_im<0 or y_im>=n:
        rotate()
        return 
    if visit[x_im][y_im]==0 or field[x_im][y_im]==1:
        
        
    