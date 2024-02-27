# [코딩테스트 연습 - 타겟 넘버 | 프로그래머스 스쿨](https://school.programmers.co.kr/learn/courses/30/lessons/43165)

def solution(numbers, target):
    def dfs(index, current_sum):
        if index == len(numbers):
            return 1 if current_sum == target else 0
        return dfs(index + 1, current_sum + numbers[index]) + dfs(index + 1, current_sum - numbers[index])

    return dfs(0, 0)

# 예시 테스트
print(solution([1, 1, 1, 1, 1], 3))  # 5
print(solution([4, 1, 2, 1], 4))     # 2
