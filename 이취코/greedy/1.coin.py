N=int(input())
array=[500,100,50,10]
count=0
for i in range(len(array)):
    count+=N//array[i]

    N%=array[i]
print(count)