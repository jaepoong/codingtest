n,k=map(int,input().split())

bag=[list(map(int,input().split())) for _ in range(n)]

bag=sorted(bag, key=lambda bag:bag[0])

for i in range(len(n)):
    for w in range(1,w+1):
        for item in bag[:-i]