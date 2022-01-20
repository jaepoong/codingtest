n=int(input())
li=[int(input()) for _ in range(n)]
dp=[1 for _ in range(n)]
dp[0]=li[0]
dp[1]=li[0]+li[1]
dp[2]=max(li[1]+li[2],li[0]+li[1])
for i in range(3,n):
    dp[i]=max(dp[i-3]+s[i-1]+s[i],dp[i-2]+s[i])

print(dp[n-1])