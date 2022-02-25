t=int(input())
for i in range(t):
    n=int(input())
    sticker=[]
    for i in range(2):
        sticker.append(list(map(int,input().split())))
    
    dp=[[0,0,0] for _ in range(n)] # 위,아래,둘다 안함
    dp[0]=[sticker[0][0],sticker[1][0],0]

    for i in range(1,n):
        dp[i][0]=max(dp[i-1][1]+sticker[0][i],dp[i-1][2]+sticker[0][i])
        dp[i][1]=max(dp[i-1][0]+sticker[1][i],dp[i-1][2]+sticker[1][i])
        dp[i][2]=max(dp[i-1][0],dp[i-1][1],dp[i-1][2])

    print(max(dp[n-1]))
