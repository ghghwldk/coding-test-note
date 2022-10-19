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

# 출력 시 필요한 distance 변수
distance = [-1] * (cityCount + 1)
# 출발도시까지의 거리는 0으로 설정
distance[startCity] = 0

# 너비 우선 탐색(BFS) 수행
# queue를 start city 기준으로 만든다.
queue = deque([startCity])
while queue:
    now = queue.popleft()
    for nextNode in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[nextNode] == -1:
            # 최단경로 갱신
            distance[nextNode] = distance[now] + 1
            queue.append(nextNode)

# 최단거리가 K인 모든 도시의 번호를 오름차순으로 출력
isExist = False
for i in range(1, cityCount+1):
    if distance[i] == distanceCondition:
        print(i)
        isExist = True

if isExist == False:
    print(-1)