# https://school.programmers.co.kr/learn/courses/30/lessons/49189

from collections import deque

def solution_drf(n, edge):

    conn_dict = dict()
    visits = [False] * n


    for e in edge:
        fir = e[0]
        sec = e[1]

        if fir in conn_dict:
            conn_dict[fir].add(sec)
        else:
            conn_dict[fir] = set([sec])

        if sec in conn_dict:
            conn_dict[sec].add(fir)
        else:
            conn_dict[sec] = set([fir])


    start = 1
    q = deque()

    while True:

        visits[start] = True
        start += 1
        print(visits)

    answer = 0
    return answer



# solution_drf(n=6,edge=[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])



from collections import deque

def solution(n, vertex):
    graph = [[] for _ in range(n + 1)]
    distance = [0] * (n + 1)  # 1번 노드부터 각 노드까지의 거리를 저장
    visited = [False] * (n + 1)  # 방문 여부를 체크하는 리스트

    # 그래프 초기화
    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)

    # BFS
    queue = deque([1])
    visited[1] = True
    while queue:
        current = queue.popleft()
        for next_node in graph[current]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)
                distance[next_node] = distance[current] + 1

    # 가장 멀리 떨어진 노드의 개수 계산
    max_distance = max(distance)
    return distance.count(max_distance)

# 예시 테스트
print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))  # 3
