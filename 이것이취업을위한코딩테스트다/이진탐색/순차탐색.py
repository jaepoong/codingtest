def sequential(target,array):
    for i in range(len(array)):
        if array[i]==target:
            return i
ar=list(input().split())
tar=input()
print(sequential(tar,ar))
