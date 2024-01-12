from collections import deque

bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]

def solution(bridge_length, weight, truck_weights):

    tq = deque(truck_weights)
    bq = deque(0 for _ in range(bridge_length))
    on_weight = 0
    sec = 0

    while tq:

        on_weight -= bq.popleft()

        truck_weight = tq.popleft()

        if on_weight + truck_weight <= weight:
            on_weight += truck_weight
            bq.append(truck_weight)
        else:
            tq.appendleft(truck_weight)
            bq.append(0)

        sec += 1

    sec += len(bq)

    return sec






print(solution(bridge_length,weight,truck_weights))












