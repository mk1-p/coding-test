# https://school.programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):

    for i in range(1, len(triangle)):

        for j, v in enumerate(triangle[i]):

            f_num = triangle[i][j]
            b_num = triangle[i][j]
            if j-1 > -1:
                f_num += triangle[i-1][j-1]
            if j+1 < len(triangle[i]):
                b_num += triangle[i-1][j]

            triangle[i][j] = max(f_num, b_num)

    return max(triangle[len(triangle)-1])


solution(triangle=[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
# 30

# 0
# 0 1
# 0 1 2
# 0 1 2 3
