import sys

nums = sys.stdin.readline().split(' ')

A = int(nums[0])
B = int(nums[1])
C = int(nums[2])

# 첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.

print(f'{(A+B)%C}')
print(f'{((A%C) + (B%C))%C}')
print(f'{(A*B)%C}')
print(f'{((A%C)*(B%C))%C}')
