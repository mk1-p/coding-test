
import copy


def solution(k, dungeons):
    answer = 0
    while k > 0 and dungeons:
        dungeons.sort(key=lambda x: k - (k - x[0]) - x[1])
        dungeon = dungeons.pop()
        if k < dungeon[0]:
            continue
        print(f'k {k} | point {k - (k - dungeon[0]) - dungeon[1]}')
        print(dungeon)
        answer += 1
        k = k - dungeon[1]

    return answer

# O(n) 안으로 만드는 메소드 실패...
# 우선순위 척도에 대한 부분이 다른 던전에 대한 것들을 무시할 수가 없는듯 하다.



# solution(k=80,dungeons=[[80,20],[50,40],[30,10]])
# return 3
# solution(k=10,dungeons=[[5, 4], [6, 1], [100, 10]])
# solution(k=100,dungeons=[[100, 98], [3, 1], [4, 2]])
solution(k=10,dungeons=[[10, 5], [2, 2], [2, 2], [2, 2], [2, 2], [2, 2]])




result = 0
N = 0
visited = []


def dfs(k, cnt, dungeons):
    global result
    if cnt > result:
        result = cnt

    for j in range(N):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            visited[j] = 0


def other_solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return result


one_line_solution = lambda k, d: max([one_line_solution(k - u, d[:i] + d[i+1:]) + 1 for i, (m, u) in enumerate(d) if k >= m] or [0])
