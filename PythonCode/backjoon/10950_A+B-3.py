import sys

N = int(sys.stdin.readline())

for i in range(N):
    nums = sys.stdin.readline().split()
    X = int(nums[0])
    Y = int(nums[1])
    print(X+Y)