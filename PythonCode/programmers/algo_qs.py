import math

# https://school.programmers.co.kr/learn/courses/30/lessons/42586
progresses1 = [93, 30, 55]
speeds1 = [1, 30, 5]
progresses2 = [95, 90, 99, 99, 80, 99]
speeds2 = [1, 1, 1, 1, 1, 1]

def func_develop(progresses, speeds):

    days = []
    answer = []

    for i in range(0, len(progresses)):
        day = math.ceil((100 - progresses[i]) / speeds[i])
        if days and days[0] < day:
            answer.append(len(days))
            days.clear()
            days.append(day)
        # elif days and days[0] == day:
        #     answer.append(len(days)+1)
        #     days.clear()
        else:
            days.append(day)

        if i == len(progresses) - 1:
            answer.append(len(days))

    return answer

print(func_develop(progresses1,speeds1))
