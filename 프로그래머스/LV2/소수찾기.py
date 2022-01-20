import math
from itertools import permutations

def eratos(n): # n 까지의 모든 소수
    array=[True for i in range(n+1)]
    for i in range(2,int(math.sqrt(n))+1):
        if array[i]==True:
            j=2
            while i*j<=n:
                array[i*j]=False
                j+=1
    array[0]=False
    array[1]=False
    return array

def solution(numbers):
    answer=0
    arr=eratos(10**(len(numbers)))
    li=list(numbers)
    for i in range(1,len(numbers)+1):
        ar=[]
        per=list(permutations(li,i))
        for j in per:
            st=""
            for k in j:
                st+=k
            if st in ar:
                continue
            ar.append(st)
        print(ar)
        for i in ar:
            if i[0] !='0' and arr[int(i)]:
                answer+=1
    print(answer)
    return answer