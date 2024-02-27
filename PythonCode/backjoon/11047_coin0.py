import sys

# 입력: 첫 번째 줄에 화폐 종류의 수(N)와 만들어야 할 가치(value)
N, value = map(int, sys.stdin.readline().split())

# 첫 번째 화폐 단위와 그 개수 계산
pre_coin = int(sys.stdin.readline())
coin_count = {pre_coin: value // pre_coin}

# 화폐 단위를 하나씩 읽으며 최소 개수 계산
for _ in range(N-1):
    coin = int(sys.stdin.readline())

    # 현재 화폐 단위가 만들어야 할 가치보다 크면 무시
    if coin > value:
        continue

    # 새로운 화폐 단위로 교체 가능한 개수 계산
    pre_count = coin_count[pre_coin]
    mul = coin // pre_coin
    replace_count = pre_count // mul

    # 새로운 화폐 단위 추가 및 이전 화폐 단위 개수 갱신
    coin_count[coin] = replace_count
    coin_count[pre_coin] = pre_count - (replace_count * mul)

    # 이전 화폐 단위 업데이트
    pre_coin = coin

# 최소 화폐 개수 출력
print(sum(coin_count.values()))
