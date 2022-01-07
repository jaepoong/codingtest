import math

def rotate_90(m): # 2차원 리스트 90도 회전
    N = len(m)
    ret = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret

def 

def is_prime_number(x): # 소수 판별
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True

def eratos(n): # n 까지의 모든 소수
    array=[True for i in range(n+1)]
    for i in range(2,int(math.sqrt(n))+1):
        if array[i]==True:
            j=2
            while i*j<=n:
                array[i*j]=False
                j+=1

