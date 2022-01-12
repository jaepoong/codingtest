import heapq
n=int(input())
x=[]
for i in range(n):
    x.append(int(input()))

heapq.heapify(x)
result=0
while len(x)>1:
    a=heapq.heappop(x)
    b=heapq.heappop(x)
    heapq.heappush(x,a+b)
    result+=(a+b)

print(result)