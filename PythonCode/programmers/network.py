# https://school.programmers.co.kr/learn/courses/30/lessons/43162

from collections import deque

def solution(n, computers):
    def bfs(start):
        queue = deque([start])
        visited[start] = True
        while queue:
            v = queue.popleft()
            for i in range(n):
                if computers[v][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True

    visited = [False] * n
    count = 0

    for i in range(n):
        if not visited[i]:
            bfs(i)
            count += 1

    return count

# 예시 테스트
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))  # 2
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))  # 1
