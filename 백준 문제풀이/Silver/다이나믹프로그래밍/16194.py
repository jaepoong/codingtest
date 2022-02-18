n=int(input())
card=[0]+list(map(int,input().split()))
li=[0]*(n+1)

for i in range(1,n+1):
    li[i]=card[1]*i
    
for i in range(1,n+1):
    for j in range(1,i+1):
        li[i]=min(li[i],li[i-j]+card[j])

print(li[n])