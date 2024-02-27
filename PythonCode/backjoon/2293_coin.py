# import sys
#
# subject = sys.stdin.readline().split()
# n = int(subject[0])
# k = int(subject[1])
# coin_values = []
#
# for _ in range(n):
#     coin_values.append(int(sys.stdin.readline()))

def solution(n, k, coins):
    print('에??')
    # 각 코인이 큰 수부터 정렬하여 하위 코인이 몇개까지 구성이 가능한가 판단한다.
    # DP 방법을 고려했을때 코인 가치의 순서로 정렬 후, 점차 큰 코인이 될때의 가치 경우의 수를 판단한다.
    # 1, 3, 5, 10
    # 3 코인은 1이 3개 구성 가능,
    # 5 코인은 3이 1개 외 1이 2개로 구성 가능
    # 이에 대한 경우의 수를 직전 코은 기준으로 개속해서 구해나간다.
    # 최종적으로 총 금액 X를 5, 3, 1 코인 기준으로 찾아나간다. 부분 최적해를 구하는 방식이다.

def coin_change_ways(n, k, coin_values):
    # DP 배열 초기화: 0으로 가치 k까지의 리스트를 만듦. 첫 번째 항목을 1로 설정 (0원을 만드는 방법은 아무것도 선택하지 않는 것)
    dp = [0] * (k + 1)
    dp[0] = 1

    # 각 동전에 대해 반복
    for coin in coin_values:
        # 현재 동전의 가치부터 k까지 반복
        for x in range(coin, k + 1):
            # 현재 가치에서 동전의 가치를 뺀 금액을 만들 수 있는 경우의 수를 추가
            dp[x] += dp[x - coin]
            print(f'coin : {coin} | x : {x} | x-c : {x-coin} | dp : {dp}')

    return dp[k]

# 예제 입력
n = 3
k = 10
coin_values = [1, 2, 5]

# 경우의 수 계산
coin_change_ways(n, k, coin_values)


# 5 1 1 1 1 1
# 5 2 1 1 1
# 5 2 2 1
# 5 5
# 2 2 2 2 2
# 2 2 2 2 1 1
# 2 2 2 1 1 1 1
# 2 2 1 1 1 1 1 1
# 2 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1