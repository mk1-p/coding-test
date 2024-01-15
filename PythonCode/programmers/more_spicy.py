from queue import PriorityQueue
import heapq

scoville = [1, 2, 3, 9, 10, 12]
K = 7
# return 2

def solution(scoville, K):

    count = 0
    heapq.heapify(scoville)
    while True:

        first_min = heapq.heappop(scoville)
        print(first_min)

        if first_min >= K:
            break
        elif first_min < K and len(scoville) == 0:
            count = -1
            break
        else:
            second_min = heapq.heappop(scoville)
            scov_point = first_min + (second_min * 2)
            heapq.heappush(scoville, scov_point)
            count += 1

    return count

# print(solution(scoville=[1, 2, 3, 9, 10, 12], K=2))
# print(solution(scoville=[1, 1, 2, 6], K=24))
# print(solution(scoville=[1, 1], K=3))
print(solution(scoville=[10, 1, 1, 1], K=10))



