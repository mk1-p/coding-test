# https://school.programmers.co.kr/learn/courses/30/lessons/42586

import math

progresses = [93, 30, 55]
speeds = [1, 30, 5]
# return [2, 1]

def solution(progresses, speeds):
    days = []
    answer = []

    for i in range(0, len(progresses)):

        day = math.ceil((100 - progresses[i]) / speeds[i])

        if days and days[0] < day:
            answer.append(len(days))
            days.clear()

        days.append(day)

        if i == len(progresses) - 1:
            answer.append(len(days))

    return answer

