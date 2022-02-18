x=int(input())
array=[0]*1001
array[1]=1
array[2]=2
for i in range(3,1000):
    array[i]=array[i-1]+array[i-2]

print(array[x])