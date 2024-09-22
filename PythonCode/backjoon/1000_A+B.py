import sys

nums = sys.stdin.readline().split(' ')
answer = 0
for i in range(len(nums)):
    answer = answer + int(nums[i])

print(answer)