import math
def eratos(n): # n 까지의 모든 소수
    array=[True for i in range(n+1)]
    for i in range(2,int(math.sqrt(n))+1):
        if array[i]==True:
            j=2
            while i*j<=n:
                array[i*j]=False
                j+=1
    return array

array=eratos(1000)
n=int(input())
x=list(map(int,input().split()))
count=0
for i in range(n):
    if array[x[i]]==True:
        count+=1

print(count)