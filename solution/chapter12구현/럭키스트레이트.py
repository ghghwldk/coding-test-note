# 특정 조건: 점수 N을 자릿수를 기준으로 반으로 나누어
#
"""
*** 특정 조건
*** 상태인지 아닌지를
*** 출력: LUCKY / READY

항상 짝수
"""

input = str(input())
length = len(input)
halfLength = length // 2
left = input[:halfLength]
right = input[-1*halfLength:]

leftSum = 0
rightSum = 0
for i in range(halfLength):
    leftSum += int(left[i])
    rightSum += int(right[i])

if leftSum == rightSum:
    print('LUCKY')
else:
    print('READY')