def binary_search(array,target,start,end):
    if start>end:
        return "no"
    mid=(start+end)//2
    if array[mid]==target:
        return "yes"
    elif array[mid]>target:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)
N=int(input())
array=list(map(int,input().split()))
M=int(input())
target=list(map(int,input().split()))
for i in target:
    print(binary_search(array,i,0,len(array)-1))