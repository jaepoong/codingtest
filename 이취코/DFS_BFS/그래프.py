inf=999999
#인접 행렬
'''graph=[[0,7,5],[7,0,inf],[5,inf,0]]
print(graph)'''
# 인접리스트 방식에서는 모든 노드에 연결된 노드의 정보를 차례로 연결
#인접 리스트
grape=[[] for _ in range(3)]

grape[0].append((1,7))

grape[0].append((2,5))

grape[1].append((0,7))

grape[2].append((0,5))

print(grape)