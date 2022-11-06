"""
본 문제에서는 Chrome 창에서의 뒤로가기 기능을 구현한다.

이를 통해 stack 활용법을 숙지하자.
"""

urls = input().split() # 과거에 방문했던 url들

for i in range(len(urls)):
    print(urls.pop())