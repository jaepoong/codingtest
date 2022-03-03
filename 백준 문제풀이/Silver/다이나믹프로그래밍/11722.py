n=int(input())
array=list(map(int,input().split()))
dp=[0]*n
dp[0]=1
for i in range(n):
     for j in range(i):
        if array[i]<array[j]:
            dp[i]=max(dp[i],dp[j]+1)
        else:
            dp[i]=max(dp[i],dp[j])

print(max(dp))