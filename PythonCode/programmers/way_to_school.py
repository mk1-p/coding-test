# https://school.programmers.co.kr/learn/courses/30/lessons/42898

# def solution1(m, n, puddles):
    # puset = set()
    # for p in puddles:
    #     puset.add(f'{p[0]-1}-{p[1] - 1}')
    #
    # routes = [[0]*m] * n
    # counts = []
    #
    # for i in range(n):
    #     for j in range(m):
    #         if i == 0 and j == 0:
    #             continue
    #         upper_num = m*n
    #         left_num = m*n
    #         if i > 0:
    #             upper_num = routes[i-1][j]
    #         if j > 0:
    #             left_num = routes[i][j-1]
    #
    #         result = min(upper_num,left_num) + 1
    #         key = f'{i}-{j}'
    #         if key in puset:
    #             print(f'{key} 풍덩')
    #             result += 10
    #         else:
    #             cnt =
    #             counts.append()
    #         routes[i][j] = result
    #         print(f'n = {i} | m = {j} | res : {result}')
    #
    # return routes[n-1][m-1] -1

def solution(m, n, puddles):
    # 경로의 수 111 방법 활용 방식 적용하였음
    # IDEA ->
    # 가로 세로 어디로가든 뒤로가지 않는다면
    # 최종 위치에 도달하기까지 거치는 수는 동일
    # 하지만 물웅덩이는 지나지 못하기 때문에 해당 웅덩이 위치는 경로 횟수를 0으로 초기화
    # 이차배열 시작 위치 [0][i] [i][0] 위치에 물웅덩이가 있을 시 그 뒤 경로는 0으로 설정

    puddle_set = set((x-1, y-1) for x, y in puddles)

    routes = [[0 for _ in range(m)] for _ in range(n)]

    # 첫 번째 행과 열 초기화
    for i in range(m):
        if (i, 0) in puddle_set:
            break
        routes[0][i] = 1

    for i in range(n):
        if (0, i) in puddle_set:
            break
        routes[i][0] = 1

    # 격자 내 각 위치에 대한 경로 계산
    for i in range(1, n):
        for j in range(1, m):
            if (j, i) in puddle_set:
                routes[i][j] = 0
            else:
                routes[i][j] = routes[i-1][j] + routes[i][j-1]

    return routes[n-1][m-1] % 1000000007





print(solution(m=4, n=3, puddles=[[3, 3],[2, 4]]))
# 4