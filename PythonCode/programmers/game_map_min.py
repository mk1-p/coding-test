# https://school.programmers.co.kr/learn/courses/30/lessons/1844
from collections import deque

def solution(maps):
    # 방향 벡터 정의 (동, 서, 남, 북)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    n, m = len(maps), len(maps[0])  # 맵의 크기

    # 방문 여부를 확인하는 2차원 리스트
    visited = [[False] * m for _ in range(n)]

    # BFS를 위한 큐
    queue = deque([(0, 0, 1)])  # 시작 위치와 시작 시의 거리

    while queue:
        x, y, dist = queue.popleft()

        # 상대 팀 진영에 도달한 경우
        if x == n - 1 and y == m - 1:
            return dist

        # 4 방향에 대해 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 맵 범위 내에 있고, 벽이 아니며, 방문하지 않은 경우
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))

    # 상대 팀 진영에 도달할 수 없는 경우
    return -1

# 예시 입력
maps1 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
maps2 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]

# 결과 출력
print(solution(maps1))  # 11
print(solution(maps2))  # -1
