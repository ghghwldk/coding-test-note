from collections import deque

cityCount, streetCount, distanceCondition, startCity = map(int, input().split())

# graph 구축
graph = [[] for i in range(cityCount + 1)]
for _ in range(streetCount):
  startPoint, endPoint = map(int, input().split())
  graph[startPoint].append(endPoint)

# distance
distances = [-1] * (cityCount + 1)
distances[startCity] = 0


def changeDistance(distances, current, distance):
  if distances[current] == -1:
    distances[current] = distance
  else:
    # 다른 길로도 방문 가능
    # 최단경로를 구하는 문제이기 때문에 아래와 같이 비교 후 대입
    if distances[current] > distance:
      distances[current] = distance


def dfs(current, distance):
  nears = graph[current]
  # 옮기자마자 거리를 계산한다.
  changeDistance(distances, current, distance)
  if len(nears) == 0:
    return
  else:
    for i in range(len(nears)):
      # python에는 '++'에 해당되는 문법이 존재하지 않는다.
      # distance를 +1로 바꾸어버리면 안된다.
      # for문 돌면서 값이 변하기 때문이다.
      dfs(nears[i], distance + 1)


dfs(startCity, 0)

isExist = False
for i in range(1, cityCount + 1):
  if distances[i] == distanceCondition:
    print(i)
    isExist = True

if not isExist:
  print(-1)
