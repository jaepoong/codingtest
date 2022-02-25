n,m=map(int,input().split())
x=[]
d=[0]*n
for i in range(n):
    x.append(int(input()))
x.sort()
for i in range(n):
    for j in range(1,m+1):
        i