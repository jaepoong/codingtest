n=int(input())
a=input().split()

space=[1,1]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
k=['R','L','U','D']


for plan in a:
    for i in range(len(k)):
        if plan==k[i]:
            dix+=dx[i]
            diy+=dy[i]
    
    if not (1<=space[0]<=n) or (1<=space[1]<=n):
        continue
    space[0]+=dix
    space[1]+=diy