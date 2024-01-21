# https://school.programmers.co.kr/learn/courses/30/lessons/42747
from collections import deque

def solution(citations):
    citations.sort()
    # n = 1000
    # m = 10000
    dqc = deque(citations)

    print(citations)
    h = []

    while dqc:
        num = dqc.popleft()
        print(f'{num} | {len(dqc)}')
        
        len(dqc) if num > len(dqc) else num
        h.append(num)

    print(h)
    return max(h)


solution(citations=[3, 0, 6, 1, 5])
# 3