n=int(input())
x=list(map(int,input().split()))
result=""
for i in range(len(x)):
    count=0
    for j in range(i,len(x)):
        if x[i]<x[j]:
            result+=str(x[j])+" "
            count+=1
            break
    if not count:
        result+="-1 "

print(result[:-1])