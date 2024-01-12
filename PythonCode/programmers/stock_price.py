from collections import deque

prices = [1, 2, 3, 2, 3]

def solution(prices):

    # 완전 탐색 O(n)
    pq = deque(prices)
    answer = []

    while pq:
        price = pq.popleft()
        for i, cp in enumerate(pq):
            print(f'{price} : {cp}')
            if price > cp:
                print(f'append {i+1}')
                answer.append(i+1)
                break
            elif i == len(pq) -1:
                answer.append(i)
        print('--------')
    answer.append(0)

    return answer


solution(prices)


def solution1(prices):
    stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        while stack != [] and stack[-1][1] > prices[i]:
            past, _ = stack.pop()
            answer[past] = i - past
        stack.append([i, prices[i]])
    for i, s in stack:
        answer[i] = len(prices) - 1 - i
    return answer

solution1(prices)