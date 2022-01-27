from collections import deque
queue=deque()
n=int(input())
k=int(input())
li=[] # 사과
for i in range(k):
    li.append(list(map(int,input().split())))

l=int(input())
direction=[list(input().split()) for _ in range(l)] # 방향 변경 시간[0], 방향[1]
dy=[0,-1,0,1]
dx=[1,0,-1,0] # 동,남,서,북
di=0
x,y=0,0
time=0
queue.append([0,0])

while True:
    time+=1
    dny=y+dy[di]
    dnx=x+dx[di]
    
    if dny < 0 or dny >=n or dnx <0 or dnx  >= n or [dny,dnx] in queue : # 벽에 부딫히면 끝
        break
    
    if [dny+1,dnx+1] in li: 
        li.remove([dny+1,dnx+1])
        
    else:    
        queue.popleft()

    queue.append([dny,dnx])
    
    y=dny
    x=dnx
    
    if time==int(direction[0][0]):
        if direction[0][1]=='L':
            di=(di-1)%4
        elif direction[0][1] == 'D':
            di=(di+1)%4
        direction.pop(0)
print(direction)
print(li)
print(time)