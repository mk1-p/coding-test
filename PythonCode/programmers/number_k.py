# https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):

    answer = []

    for command in commands:


        i = command[0] - 1
        j = command[1]
        k = command[2] - 1

        target_arr = array[i:j]
        target_arr.sort()
        answer.append(target_arr[k])

    return answer

solution(array=[1, 5, 2, 6, 3, 7, 4], commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]])
# return [5, 6, 3]



def solution_other(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))