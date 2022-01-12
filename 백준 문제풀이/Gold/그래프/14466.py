n,k,r= map(int,input().split())
bridge=[list(map(int,input().split())) for _ in range(r)]

field=[[0]*n for _ in range(n)]
go=[[[]*n for _ in range(n)] for _ in range(n)]
cow=[list(map(int,input().split())) for _ in range(k)]

for i in bridge:
    go[i[0]][i[1]].append([i[2],i[3]])
    go[i[2]][i[3]].append([i[0],i[1]])
for i in cow:
    field[i[0]][i[1]]=1

print(go)
print(cow)
print(field)