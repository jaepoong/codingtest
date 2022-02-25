array=[7,5,3,2,4,1,2]
count=0
for i in range(len(array)):
    min_index=i
    for j in range(i+1,len(array)):
        if array[min_index]>array[j]:
            count+=1
            min_index=j
    array[i], array[min_index] = array[min_index], array[i]
print(array,count)