# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):

    vir = 0
    hor = 0
    for size in sizes:
        x = size[0]
        y = size[1]
        if x >= y:
            vir = x if x >= vir else vir
            hor = y if y >= hor else hor
        else:
            vir = y if y >= vir else vir
            hor = x if x >= hor else hor

    print(vir * hor)
    return vir * hor


solution(sizes=[[60, 50], [30, 70], [60, 30], [80, 40]])
# 4000
solution(sizes=[[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])
# 120
solution(sizes=[[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]])
# 133