# 탑 다운 방식
d=[0]*100
def fibo(x):
    print(x, end="   ")
    if x==1 or x==0:
        return 1
    if d[x]!=0:
        return d[x]
    d[x]=fibo(x-1)+fibo(x-2)
    return d[x]
a=int(input("피보나치 수열로 변환합니다.: "))
print(fibo(a))