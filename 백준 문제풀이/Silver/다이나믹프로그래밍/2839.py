n=int(input())
d=[5001]*(n+1)
d[0]=0
for i in (3,5):
    for j in range(i,n+1):
        if d[j-i]!=5001:
            d[j]=d[j-i]+1
if d[n]==5001:
    print(-1)
else:
    print(d[n])