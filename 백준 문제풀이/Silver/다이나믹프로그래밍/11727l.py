n=int(input())
array=[0]*1001
array[1]=1
array[2]=3
for i in range(3,1001):
    array[i]=array[i-1]+array[i-2]*2
print(array[n]%10007)