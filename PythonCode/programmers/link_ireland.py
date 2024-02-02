# https://school.programmers.co.kr/learn/courses/30/lessons/42861

def solution1(n, costs):

    seom_dict = dict()
    is_visits = [False for _ in range(n)]
    link_counts = [0 for _ in range(n)]
    cnt = 0
    total_cost = 0

    for cost in costs:
        s1 = cost[0]
        s2 = cost[1]
        co = cost[2]

        link_counts[s1] += 1
        link_counts[s2] += 1

        tp1 = (s2, co)
        tp2 = (s1, co)

        # if seom_dict[s1]:
        #     seom_dict[s1].append(tp1)
        # else:
        #     seom_dict[s1] = []
        #     seom_dict[s1].append(tp1)
        #
        # if seom_dict[s2]:
        #     seom_dict[s2].append(tp2)
        # else:
        #     seom_dict[s2] = []
        #     seom_dict[s2].append(tp2)

    costs.sort(key=lambda x:100-x[2]+link_counts[x[0]]+link_counts[x[1]])
    loop_cnt = 0
    while True:
        cost = costs.pop()
        s1 = cost[0]
        s2 = cost[1]
        co = cost[2]

        if is_visits[s1] is False or is_visits[s2] is False:
            total_cost += co

            if is_visits[s1] is False:
                is_visits[s1] = True
                cnt += 1
            if is_visits[s2] is False:
                is_visits[s2] = True
                cnt += 1

        loop_cnt += 1
        print(f'loop cnt : {loop_cnt} | visit : {is_visits}')
        print(f'costs : {costs}')

        if cnt == n:
            break

    print(is_visits)
    print(total_cost)
    return total_cost


from collections import deque
class Link:
    def __init__(self, cost, point):
        self.cost = cost
        self.point = point


def solution(n, costs):

    is_visits = [False for _ in range(n)]
    # costs.sort(key=lambda x:x[0])
    link_dict = {}

    for cost in costs:
        co = cost[2]
        s1 = cost[0]
        s2 = cost[1]

        if s1 not in link_dict:
            link_dict[s1] = []
        link_dict[s1].append(Link(co, s2))

        if s2 not in link_dict:
            link_dict[s2] = []
        link_dict[s2].append(Link(co, s1))


    sp = 0
    visit_cnt = 0
    total_cost = 0
    print(link_dict)
    while True:

        if is_visits[sp]:
            sp += 1
            continue

        links = link_dict[sp]
        links.sort(key=lambda x:x.cost)

        print(f'출발 포인트 {sp}')
        for link in links:
            conn_p = link.point
            cost = link.cost
            if is_visits[conn_p]:
                continue
            else:
                print(f'추가되는 코스트 {cost} | 링크 : {conn_p}')
                is_visits[sp] = True
                is_visits[conn_p] = True

                total_cost += cost
                break

        if sp == n-1:
            print("sp max")
            break

    print(total_cost)
    return total_cost







solution(n=4, costs=[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])
# 4