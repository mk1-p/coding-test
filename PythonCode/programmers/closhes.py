from itertools import *
from functools import reduce


input1 = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
# return 5

input2 = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
# return 3


def multiply(arr):
    result = 1
    for v in arr:
        result = result * v
    return result

def solution(clothes):
    dict_clothes = dict()

    for cloth in clothes:
        key = cloth[1]
        if key in dict_clothes:
            dict_clothes[key] += 1
        else:
            dict_clothes[key] = 1

    nums = dict_clothes.values()

    cases = []
    for i in range(1,len(nums)+1):
        cases.extend(list(combinations(nums, i)))

    answer = 0
    for case in cases:
        print(case)
        answer += multiply(case)

    return answer





print(solution(input1))