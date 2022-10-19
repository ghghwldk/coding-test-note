'''
1~N번까지의 도시 존재
M개의 단방향 도로 존재

모든 도로의 거리는 1

특정 도시 X로부터 출발하여 최단거리가 정확히 K인 모든 도시들의 번호를 출력하는 프로그램 작성

[입력]
1째 줄
도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X

2째 줄부터
A, B: A-B 연결 되었다는 의미

[출력]
도시 번호 줄바꿈하여 출력
없으면, -1 출력
'''
from collections import deque

cityCount, streetCount, distanceCondition, startCity = map(int, input().split())
# graph 연결 정보 입력
graph = [[] for _ in range(cityCount + 1)]

for _ in range(streetCount):
    startPoint, endPoint = map(int, input().split())
    graph[startPoint].append(endPoint)

# 출발도시로부터 특정 노드까지의 거리를 저장하기 위한 Array
distance = [-1] * (cityCount + 1)
# 출발도시까지의 거리는 0으로 설정
distance[startCity] = 0

# 너비 우선 탐색(BFS) 수행
# queue를 start city 기준으로 만든다.
"""
BFS는 시작점의 인접한 정점들을 차례로 모두 방문하고, 
방문했던 정점을 시작점으로 해서 다시 인접한 정점들을 
차례로 모두 방문하고 하는 방식으로, 너비 우선 탐색이라고 부릅니다.
"""
# BFS는 시작점의 인접한 정점들을 차례로 방문하기 때문에 시작점을 Queue에 넣어 준다.
queue = deque([startCity])
while queue:
    # 출발지와 연결된 노드를 시작점으로 하여 한단계 더 멀리 존재하는 노드를 추적하기 위해
    # 새로운 출발점을 잡는다.
    now = queue.popleft()
    # 새로운 출발점과 연결된 다음 노드를 탐색한다.
    for nextNode in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[nextNode] == -1:
            # 시작으로부터 최단경로 갱신한다.
            # 이 문제에서는 노드간 거리가 1이므로 +1을 한다.
            # 노드간 거리가 1이 아니라면, 문제에서 주어진 간선간 거리를 더해주면 된다.
            distance[nextNode] = distance[now] + 1
            # 방문했던 정점을 시작점으로 해서 다시 인접한 정점들을 차례로 방문하기 위해
            # Queue에 방문했던 정점을 추가한다.
            queue.append(nextNode)

# 최단거리가 K인 모든 도시의 번호를 오름차순으로 출력
isExist = False
for i in range(1, cityCount+1):
    if distance[i] == distanceCondition:
        print(i)
        isExist = True

if isExist == False:
    print(-1)