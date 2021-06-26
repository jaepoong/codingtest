row,column=map(int,input().split())
(x,y,f_d)=map(int,input().split())
x=[]
for _ in range(row):
    x.append(list(map(int,input().split())))
dx=[-1,1,0,0]
dy=[0,0,-1,1]
direct=[0,1,2,3]
while True:
