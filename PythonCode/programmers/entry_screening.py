# https://school.programmers.co.kr/learn/courses/30/lessons/43238


def solution(n, times):
    a,b = 0,1
    while not is_ok(n, times, b):
        a,b = b, 2*b
    while a<b:
        m = (a+b)//2
        a,b = (a,m) if is_ok(n, times, m) else (m+1,b)
    return a

def is_ok(n, times, x):
    return n <= sum(x//i for i in times)