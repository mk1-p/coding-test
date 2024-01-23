# https://school.programmers.co.kr/learn/courses/30/lessons/42839


from itertools import permutations

def solution(numbers):
    answer = 0
    candits = set()
    length = len(numbers)
    numbers = list(map(str, numbers))

    # extract candidates
    for i in range(1, length+1):
        permute = list(permutations(numbers, i))
        permute = set(list(map(lambda x: int(''.join(x)), permute)))
        candits = candits.union(permute)
    candits = list(filter(lambda x: x>1, list(candits)))

    # prime number
    for num in list(candits):
        flag = True
        for i in range(2, num//2+1):
            if not flag:
                break
            if num % i == 0:
                flag = False

        if flag:
            answer += 1

    return answer


solution(numbers="17")
# 3 - 7, 17, 71
solution(numbers="011")
# 2 - 11, 101