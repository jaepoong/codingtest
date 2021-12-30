n=int(input())
length=list(map(int,input().split()))
d=[0]*101
d[0]=length[0]
d[1]=max(length[0],length[1])
for i in range(2,n):
    d[i]=max(d[i-2]+length[i],d[i-1])
print(d[n-1])