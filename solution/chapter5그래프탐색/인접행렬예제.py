INF = 999999999 # 무한의 비용 선언

# Node i에서 j로 
# 가는 길이 있으면, 거리를 입력
# 가는 길이 없으면, INF를 입력
graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0],
]

print(graph)