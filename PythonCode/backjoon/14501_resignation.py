# https://www.acmicpc.net/problem/14501

import sys

N = int(sys.stdin.readline())

schedules = []

for x in range(int(N)):
    input = sys.stdin.readline()
    temp = input.split()
    day = int((temp[0]))
    pay = int(temp[1])
    schedules.append((day, pay))

def solution(N, schedules):

    max_benefit = schedules[0]
    max_value = max_benefit[1]/max_benefit[0]
    rest_day = max_benefit[0]
    total_pay = 0

    print(schedules)

    count = 1
    while count <= len(schedules):
        i = count
        count += 1

        rest_day -= 1

        if rest_day == 0:
            print(f'finish : {max_benefit}')
            total_pay += max_benefit[1]
            max_value = 0

        if i >= len(schedules):
            continue

        benefit = schedules[i]
        value = benefit[1] / benefit[0]


        if benefit[0] + i -1 > N:
            continue

        if max_value > value or max_value == value:
            continue

        rest_day = benefit[0]
        max_benefit = benefit
        max_value = value

    return total_pay

print(solution(N=N, schedules=schedules))
