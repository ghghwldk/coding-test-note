# python에서 queue와 dequeue의 차이점
from collections import deque

a_list = deque()
a_list.append(1)
a_list.append(2)
a_list.append(3)
a_list.append(4)
a_list.append(5)
a_list.append(6)

print(a_list)
print(a_list.pop())
print(a_list.popleft())
# result
print(a_list)

for idx in range(len(a_list)):
    print(a_list[idx])
