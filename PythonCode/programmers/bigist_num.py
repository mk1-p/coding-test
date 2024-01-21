# https://school.programmers.co.kr/learn/courses/30/lessons/42746
import functools


def solution(numbers):
    answer = ''

    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)

    for i in numbers:
        answer += i

    return str(int(answer))


solution(numbers=[6, 10, 2])
# "6210"
solution(numbers=[3, 30, 34, 5, 9])
# "9534330"

solution(numbers=[6, 660, 43, 58])