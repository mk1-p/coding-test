import sys
import io

input_string = '''5 3
5 4 3 2 1
1 3
2 4
5 5'''

sys.stdin = io.StringIO(input_string)

# N, M = map(int, input().split())
#
# input_str = input()
# nums = [int(num) for num in input_str.split()]
#
# for _ in range(M):
#     i, j = map(int, input().split())
#     # nums에서 i, j 인덱스 사이(포함) 값의 합
#     print(sum(nums[i-1:j]))


import sys

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

# 누적 합 계산
prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

# 쿼리 처리
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(prefix_sum[j] - prefix_sum[i - 1])
