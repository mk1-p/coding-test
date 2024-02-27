# https://www.acmicpc.net/problem/1912

import sys

n = int(sys.stdin.readline())
numbers = sys.stdin.readline()
numbers = numbers.split()
numbers = [int(x) for x in numbers]

def solution(numbers):

    max_sum = numbers[0]

    for i in range(1, len(numbers)):
        numbers[i] = max(numbers[i], numbers[i] + numbers[i-1])
        max_sum = max(numbers[i], max_sum)

    return max_sum

# solution(numbers) 인트 반환했다고 틀린다느게ㅐ ㅁㅁ러ㅏㅁ니롲먀ㅏㅣ로밎
print(solution(numbers))