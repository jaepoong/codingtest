n=int(input())
li=list(map(int,input().split()))
li.sort(reverse=True)
x=li[0]
result=0
for i in range(len(li)):
    x-=1
    if x==0:
        x=li[i]
        result+=1

print(result)