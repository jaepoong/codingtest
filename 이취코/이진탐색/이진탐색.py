def binary_search(array,target,start,end):
    if start>end:
        return None
    center=(start+end)//2
    if array[center]==target:
        return center
    if array[center]>target:
        return binary_search(array,target,start,center-1)
    else:
        return binary_search(array,target,center+1,end)
n,target=map(int,input().split())
array=list(map(int,input().split()))

result=binary_search(array,target,0,n-1)
print(result)
