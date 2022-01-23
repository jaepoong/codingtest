n=int(input())
li=list(map(int,input().split()))
li.sort()
count=0
result=0
for i in range(len(li)):
    count+=1
    if count>=i:
        result+=1
        count=0

print(result)