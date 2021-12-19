N=int(input())
x=[]
y=[1 for _ in range(N)]
for i in range(N):
    x.append(list(map(int,input().split())))
for i in range(N):
    for j in range(N):
        if(x[j][0]>x[i][0] and x[j][1]>x[i][1]):
            y[i]+=1
for i in range(N):
    print(y[i],end=" ")