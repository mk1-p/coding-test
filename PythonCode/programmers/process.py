# https://school.programmers.co.kr/learn/courses/30/lessons/42587

import queue

priorities = [1, 1, 9, 1, 1, 1]
location = 0
# return 5

from collections import deque

def solution(priorities, location):
    deq = deque()
    sort_prior = sorted(priorities)

    for i, v in enumerate(priorities):
        deq.append((i, v))

    count = 0
    while deq:
        # 최대 우선순위 값을 매번 갱신
        max_pv = sort_prior[len(sort_prior) - 1]
        # 현재 첫번째 Value
        process = deq.popleft()

        # 최대 우선순위 시, location 비교
        if max_pv == process[1]:
            count += 1
            # 현재 남은 최대 우선순위 추출
            sort_prior.pop()
            if process[0] == location:
                return count
        else:
            deq.append(process)






print(solution(priorities, location))