


import sys

N = int(sys.stdin.readline())
dps = [0 for _ in range(N)]
dps[0] = 1
for i in range(1, N):
    if i == 1:
        dps[i] = 2
    else:
        dps[i] = dps[i - 2] * 2 + 1

print(dps[N-1])


N = int(sys.stdin.readline())
dps = [0] * 1001  # 1000까지의 값을 저장할 수 있는 크기로 초기화
dps[1] = 1
dps[2] = 2
for i in range(3, N + 1):
    dps[i] = (dps[i - 1] + dps[i - 2]) % 10007

print(dps[N])