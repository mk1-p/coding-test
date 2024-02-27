import sys

N = int(sys.stdin.readline())

peoples = [int(item) for item in sys.stdin.readline().split()]

peoples.sort()

total = peoples[0]
for i in range(1, N):
    time = peoples[i] + peoples[i-1]
    peoples[i] = time
    total += time

print(total)