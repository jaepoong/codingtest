import math
n=int(input())
array=[]
i=0
while True:
    i+=1
    if i**2>100000:
        break
    array.append(i**2)

result=[ 1*k for k in range(n+1)]

for i in range(4,n+1):
    for j in range(len(array)):
        if array[j]>i:
            break
        result[i]=min(result[i],result[i-array[j]]+1)

print(result[n])
    