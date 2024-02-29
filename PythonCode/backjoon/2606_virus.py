# https://www.acmicpc.net/problem/2606

# Top Down
# 재귀 스택으로 인해 Runtime 에러가 발생하는듯 함.
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

link_dict = dict()
visits = [False for _ in range(N)]
vl = set()

for _ in range(M):
    c1, c2 = map(int, sys.stdin.readline().split())

    if c1 not in link_dict: link_dict[c1] = set()
    if c2 not in link_dict: link_dict[c2] = set()

    link_dict[c2].add(c1)
    link_dict[c1].add(c2)
def check_link(key):
    vi = key - 1

    if visits[vi] == True:
        return

    visits[vi] = True
    links = link_dict[key]
    no_visits = [i for i in links if visits[i - 1] == False]

    for nv in no_visits:
        check_link(nv)
        vl.add(nv)

check_link(1)

print(len(vl))


# Bottom Up
from collections import deque

N = int(input())  # 노드의 수 입력
M = int(input())  # 엣지의 수 입력

link_dict = {}  # 각 노드의 연결 정보를 저장할 딕셔너리
visits = [False] * N  # 각 노드의 방문 여부를 저장할 리스트

for _ in range(M):
    c1, c2 = map(int, input().split())
    if c1 not in link_dict:
        link_dict[c1] = set()
    if c2 not in link_dict:
        link_dict[c2] = set()
    link_dict[c1].add(c2)
    link_dict[c2].add(c1)

def bfs(start):
    queue = deque([start])  # 시작 노드를 큐에 넣는다
    visited = set()  # 방문한 노드를 기록할 집합
    visits[start - 1] = True

    while queue:
        node = queue.popleft()
        if node in link_dict:  # 현재 노드와 연결된 노드들을 확인
            for next_node in link_dict[node]:
                if not visits[next_node - 1]:
                    visits[next_node - 1] = True
                    queue.append(next_node)
                    visited.add(next_node)
    return visited

vl = bfs(1)
print(len(vl))
