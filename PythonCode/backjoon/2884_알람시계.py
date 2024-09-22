import sys

nums = list(map(int, sys.stdin.readline().split()))
hour = nums[0]
minute = nums[1]

minute = minute - 45

if minute < 0:
    hour -= 1
    hour = hour if hour >= 0 else 23
    minute = 60 + minute

print(f"{hour} {minute}")