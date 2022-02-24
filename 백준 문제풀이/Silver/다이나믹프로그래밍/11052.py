n=int(input())
card=list(map(int,input().split()))
li=[0]*(n+1)
li[1]=card[1]
for i in range(2,n+1):
    for j in range(1,i+1):
        li[i]=max(li[i],li[i-j]+card[j])

print(li[n])