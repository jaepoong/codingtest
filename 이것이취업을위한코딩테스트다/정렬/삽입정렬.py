array=[7,5,3,2,4,1,2]
count=0
for i in range(1,len(array)):
    for j in range(i,0,-1):
        if array[j]<array[j-1]:
            array[j],array[j-1]=array[j-1],array[j]
            count+=1
        else:
            break
print(array,count)