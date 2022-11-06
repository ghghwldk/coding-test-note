"""
문제입니다!

손님이 5명이 방문합니다.
은행원 2명이 손님을 응대해야 합니다.
각 은행원이 맡을 손님의 리스트를 한 번에 출력해 주세요!

n: 손님 명수
e: 은행원 명수

"""
from collections import deque

n = int(input()) # 손님 명수
e = int(input()) # 은행원 명수
queues = list() #  은행원이 담당할 손님의 큐 리스트

# 은행원의 명수만큼 대기열 선언
for i in range(e):
    queues.append(deque())

# 선언된 대기열에 손님 추가
for i in range(1, n+1):
    queueIdx = (i-1) % e
    queues[queueIdx].append(i)
    '''
    은행원이 2명일 때
    
    0 > 0
    1 > 1
    2 > 0
    3 > 1
    '''

# 대기열에 존재하는 손님 리스트 출력
for i in range(1, e+1):
    print(str(i) + "번째 은행원-------------------------------")
    currentQueue = queues[i-1]
    for j in range(len(currentQueue)):
        print(str(currentQueue.popleft()) + "번째 손님")



