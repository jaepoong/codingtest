import math
def eratos(n): # n 까지의 모든 소수
    array=[True for i in range(n+1)]
    for i in range(2,int(math.sqrt(n))+1):
        if array[i]==True:
            j=2
            while i*j<=n:
                array[i*j]=False
                j+=1
    return [i for i in range(2,n) if array[i]==True]

array=eratos(1000001)

while True:
    n=int(input())
    if n==0:
        break

    for i in range(len(array)):
        if n-array[i] in array:
            print(str(n)+" = "+str(array[i])+" + "+str(n-array[i]))
            break