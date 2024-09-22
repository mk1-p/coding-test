import sys
first = int(sys.stdin.readline())
second = sys.stdin.readline()

for i in range(2, -1, -1):
    print(first * int(second[i]))

print(first * int(second))
