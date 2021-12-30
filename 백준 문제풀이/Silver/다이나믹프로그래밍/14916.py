n=int(input())
d=[100001]*(n+1)
coin=[2,5]
d[0]=0
for i in coin:
    for j in range(i,len(d)):
        if d[j-i]!=100001:
            d[j]=d[j-i]+1

if d[n]==100001:
    print(-1)
else:
    print(d[n])