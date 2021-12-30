n,m=map(int,input().split())
coin=[]
for i in range(n):
    coin.append(int(input()))
coin=sorted(coin)
d=[10001]*(m+1)
d=[0]=0
for i in range(4):
    for j in range(coin[i],m+1):
        if d[j-coin[i]]!=10001:
            d[j]=min(d[j],d[j-coin[i]]+1)

