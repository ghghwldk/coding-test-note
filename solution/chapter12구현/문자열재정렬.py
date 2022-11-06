'''
알파벳 대문자 & 숫자로만 구성된 입력

알파벳은 오름차순 정렬한 것을 출력한 뒤
그 뒤 숫자를 더한 값 이어서 출력
'''

input = str(input())
charList = list()
intSum = 0
strPart = ''
result = ''

for i in range(len(input)):
    current = input[i]
    if current >= 'A' and current <= 'Z':
        charList.append(current)
    else:
        intSum += int(current)

charList.sort()

for current in charList:
    strPart += current

result = strPart + str(intSum)
print(input)
print(result)